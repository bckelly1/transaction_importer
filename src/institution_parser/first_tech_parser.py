from bs4 import BeautifulSoup

import datetime
import logging


logger = logging.getLogger('first_tech_parser')


def handle_first_tech_transaction(text, headers):
    return parse_html(text, headers)


# With Bank accounts, you have to determine if the money is going in (credit) or going out (debit)
#  For First Tech, you can either determine that by looking for the parentheses () or the Credit/Debit label
def determine_transaction_style(soup):
    token = soup.find('div', attrs={'class': 'transactions-table-header'}).text.strip().split(' ')[0]
    if token == 'Deposits':
        return 'Credit'
    elif token == 'Withdrawals':
        return 'Debit'
    else:
        # TODO: Problem!
        logger.error("Could not determine transaction style!")
        return 'Unknown'


# Is the money just moving between two user-owned accounts? While that does count as a Credit/Debit, in the grand scheme
#   Of things, it doesn't affect the budget.  Mark the transaction as a transfer and it will be ignored.
def is_transfer(title):
    if 'Regular Payment Transfer' in title:
        return False
    elif 'Transfer' in title:
        return True
    elif is_credit_card_payment(title):
        return True
    else:
        return False


# Credit card payments do and don't matter. They do matter because the money is literally leaving your bank account. On
#   The other hand, you already spent the money, so the money is "gone" already, so we can think of the credit card
#   Payment more as a transfer than as "money going out".  Let the rage debate commence.
def is_credit_card_payment(title):
    # Fidelity is a bit obnoxious about this. No email on payments. Have to infer it when the money goes out.
    if 'CARDMEMBER SERV - WEB PYMT' in title:
        return True
    return False


# Example input: Deposit Transfer From ******1234
# Output: 1234
def transfer_source_account(title):
    tokens = title.split(' ')
    for token in tokens:
        if '*' in token:
            return token.replace('*', '')
    return 'Unknown Source Account'


# Main handling of the transaction email. Read the transaction and extract transaction details from the text.
def parse_email_transactions(transaction, headers):
    transaction_date = headers['Date']
    transaction_details_original = transaction.find('td', attrs={'class': 'details'}).text.strip()
    transaction_tokens = transaction_details_original.split(' ')
    merchant_tokens = []
    for n in range(2, len(transaction_tokens)):
        merchant_tokens.append(transaction_tokens[n])
    merchant = ' '.join(merchant_tokens)
    transaction_amount = transaction.find('td', attrs={'class': 'trans-amount'}).text.strip().replace('$', '').replace(',', '')
    transfer = is_transfer(transaction_details_original)
    source_account = transfer_source_account(transaction_details_original) if transfer else None
    if '(' in transaction_amount:
        amount = float(transaction_amount.replace('(', '').replace(')', ''))
        transaction_type = 'Debit'
    else:
        amount = float(transaction_amount)
        transaction_type = 'Credit'
    if 'Transfer' in transaction_details_original:
        # Most likely this is a cross-account transfer, vendor/merchant is bank
        merchant = 'First Tech'
        category = 'Transfer'
    elif 'Dividend' in transaction_details_original:
        # Credit Dividend transaction, vendor/merchant is bank
        merchant = 'First Tech'
        category = 'Dividend'
    else:
        category = ''
    logger.info('Info:')
    logger.info("\tDate: " + datetime.datetime.strftime(transaction_date, '%d/%m/%Y'))
    logger.info("\tDetail: " + merchant)
    logger.info("\tAmount: " + transaction_amount)

    return {
        'date': headers['Date'],
        'description': merchant,
        'original_description': transaction_details_original,
        'amount': amount,
        'transaction_type': transaction_type,
        'category': category,
        'merchant': source_account if transfer else merchant,
        'account_number': source_account,
        'notes': 'First Tech'
    }


# Parse the email's HTML text and extract relevant transaction info from it.
def parse_html(text, headers):
    soup = BeautifulSoup(text, features='html.parser')
    title = soup.body.find('h1', attrs={'id': 'title'}).text.strip()
    account_name = " ".join(soup.body.find_all('strong')[0].text.strip().split(' - ')[0].split())
    account_number = soup.body.find_all('strong')[0].text.strip().split(' - ')[1].replace('*', '')
    balance = soup.body.find_all(lambda tag: tag.name == 'p' and 'Balance: ' in tag.text)[0].text.split('Balance: ')[1].strip()

    logger.info('Title: ' + title)
    logger.info('Account Name: ' + account_name)
    logger.info('Account Number: ' + account_number)
    logger.info('Balance: ' + balance)

    transaction_style = determine_transaction_style(soup)
    transaction_array = []
    transactions = soup.body.find_all('tr', attrs={'class': 'transaction-row'})
    for transaction in transactions:
        parsed_transaction = parse_email_transactions(transaction, headers)
        if transaction_style != parsed_transaction.get('transaction_type'):
            logger.error("Transaction style does not match parsed transaction type from transaction!")
        if parsed_transaction['merchant'] is None or parsed_transaction['merchant'] == '':
            parsed_transaction['merchant'] = account_name
        parsed_transaction['account_number'] = account_number  # TODO: possibly redundant?
        transaction_array.append(parsed_transaction)
    return transaction_array


# In the main body of the email, figure out which account we are extracting the balance of.
def parse_account_info(soup):
    title = soup.body.find('h1', attrs={'id': 'title'}).text.strip()
    logger.info('Title: ' + title)
    accounts = soup.body.find_all('strong')
    parsed_accounts = []
    for account in accounts:
        parsed_accounts.append(parse_account(account))

    return parsed_accounts


# For each account in the email, extract the account details
def parse_account(account):
    account_parent = account.parent
    account_name = " ".join(account.text.strip().split(' - ')[0].split())
    account_number = account.text.strip().split(' - ')[1].replace('*', '').replace('#', '')
    balance = account_parent.text.split('Current Balance: ')[1].split('Available Balance')[0].replace('$', '').replace(',', '')

    logger.info('Account Name: ' + account_name)
    logger.info('Account Number: ' + account_number)
    logger.info('Balance: ' + balance)

    return {'name': account_name, 'number': account_number, 'balance': float(balance)}


# Extract all account details from the balance summary email
def handle_first_tech_balance_summary(text):
    soup = BeautifulSoup(text, features='html.parser')
    parsed_accounts = parse_account_info(soup)
    return parsed_accounts

