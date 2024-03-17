import config
import mysql.connector
import os


# Global Variable, gets opened on every request and re-closed at the end. Would be nice to use a connection pool, class
#   Variables, transaction management, and all.
db_connection = None


# As it seems, create a connection to the mysql db
def connect_to_database():
    cnx = mysql.connector.connect(
        user=os.environ.get('DATABASE_USERNAME'),
        password=os.environ.get('DATABASE_PASSWORD'),
        host=os.environ.get('DATABASE_HOSTNAME'),
        database=os.environ.get('DATABASE_NAME')
    )
    return cnx


def update_account_balance(account):
    global db_connection
    db_connection = connect_to_database()
    statement = ("update finance_accounts "
                 "set balance = %s,"
                 "last_updated = now() "
                 "where alias = %s")

    data = (
        account['balance'],
        account['number'],
    )

    cursor = db_connection.cursor()
    cursor.execute(statement, data)

    # Make sure data is committed to the database
    db_connection.commit()
    cursor.close()
    close_database()


# Find related fields to the transaction and insert the transaction as a new row
def add_transaction(transaction, message_id):
    global db_connection
    db_connection = connect_to_database()
    category_id = find_category_id(transaction['category'])
    merchant_id = find_vendor_id(transaction['merchant'])
    account_id = find_account_id(transaction['account_number'])
    inserted_id = insert_transaction(transaction, message_id, category_id, merchant_id, account_id)
    close_database()
    return inserted_id


def insert_transaction(transaction, message_id, category_id, merchant_id, account_id):
    statement = ("INSERT INTO finance_transactions "
                 "(date, description, original_description, amount, transaction_type, category, merchant, account, "
                 "mail_message_id, notes) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

    data = (
        transaction['date'],  # Should be a datetime by the time it appears here
        transaction['description'],
        transaction['original_description'],
        transaction['amount'],  # Should be a double/float by the time it appears here
        transaction['transaction_type'],
        category_id,
        merchant_id,
        account_id,
        message_id,
        transaction['notes']
    )

    cursor = db_connection.cursor()
    # Insert new transaction
    cursor.execute(statement, data)

    # Make sure data is committed to the database
    db_connection.commit()
    cursor.close()
    return cursor.lastrowid


def find_category_id(search_string):
    query = ("SELECT id, name FROM finance_categories "
             "WHERE name = %s")

    data = (search_string,)
    cursor = db_connection.cursor()
    cursor.execute(query, data)

    category_id = extract_id(cursor, search_string, "finance_categories")
    if category_id is None:
        print(f"Creating category with name {search_string}")
        category_id = insert_category(search_string, None)
    cursor.close()
    return category_id


def find_vendor_id(search_string):
    if search_string is None or search_string == '':
        raise Exception("Vendor string cannot be empty")

    query = ("SELECT id, name FROM finance_vendors "
             "WHERE name = %s")

    cursor = db_connection.cursor()
    cursor.execute(query, (search_string,))

    vendor_id = extract_id(cursor, search_string, "finance_vendors")
    if vendor_id is None:
        print(f"Creating vendor with name {search_string}")
        vendor_id = insert_new_vendor(search_string)
    cursor.close()
    return vendor_id


def find_account_id(search_string):
    query = ("SELECT id, name FROM finance_accounts "
             "WHERE (name = %s OR alias like %s)")

    cursor = db_connection.cursor()
    cursor.execute(query, (search_string, "%"+search_string+"%"))

    account_id = extract_id(cursor, search_string, "finance_accounts")
    if account_id is None:
        print(f"Creating account with name {search_string}")
        account_id = insert_new_account(search_string)
    cursor.close()
    return account_id


def insert_category(category_name, parent_id):
    statement = ("INSERT INTO finance_categories "
                 "(name, parent_category) "
                 "VALUES (%s, %s)")

    data = (
        category_name,
        parent_id
    )

    return insert_to_db(statement, data)


def insert_new_account(account_name):
    statement = ("INSERT INTO finance_accounts "
                 "(name, balance) "
                 "VALUES (%s, %s)")

    data = (
        account_name,
        0.00
    )

    return insert_to_db(statement, data)


def insert_new_vendor(vendor_name):
    statement = ("INSERT INTO finance_vendors "
                 "(name) "
                 "VALUES (%s)")

    data = (
        vendor_name,
    )

    return insert_to_db(statement, data)


# TODO: Not super pleased with using the global cursor here
def extract_id(cursor, search_string, table_name):
    query_id = None
    for (id, name) in cursor:
        if query_id is None:
            query_id = id
        else:
            raise Exception(f"Found multiple entries for query {search_string} in {table_name}")
    if query_id is None:
        print(f"Found no entries for query {search_string} in {table_name}")
    return query_id


def insert_to_db(statement, data):
    # Insert new vendor
    cursor = db_connection.cursor()
    cursor.execute(statement, data)

    # Make sure data is committed to the database
    db_connection.commit()
    last_row_id = cursor.lastrowid
    cursor.close()
    return last_row_id


def close_database():
    global db_connection
    db_connection.close()
