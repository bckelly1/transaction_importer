import logging

from database import *
from file_operations import *
from google_grabber import *
from category_inferer import *
from mail_parser import *

from enum import Enum

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


logger = logging.getLogger('mail_handler')


class EmailType(Enum):
    TRANSACTION = 'Transaction'
    BALANCE_SUMMARY = 'Balance Summary'


def handle_transaction_email(email_fields):
    transactions = extract_transactions(email_fields)
    message_id = email_fields['message_id']
    for transaction in transactions:
        if transaction['category'] is None or transaction['category'] == '':
            transaction['category'] = infer_category(transaction['description'])
        add_transaction(transaction, message_id)
    time_string = datetime.datetime.strftime(email_fields['headers']['date'], "%m/%d/%Y, %H:%M:%S")
    logger.info('Parsed message "' + email_fields['subject'] + '" from ' + time_string)


def handle_balance_summary_email(email_fields):
    accounts = extract_accounts(email_fields)
    for account in accounts:
        update_account_balance(account)


def handle_email_message(email_type, email_fields):
    if email_type == EmailType.TRANSACTION:
        handle_transaction_email(email_fields)
    elif email_type == EmailType.BALANCE_SUMMARY:
        handle_balance_summary_email(email_fields)


def run_financial_email_queries(mailbox):
    results = {'messages': []}
    transaction_results = query_transactions(mailbox)

    # TODO: Feels kinda hacky I just want to merge the dictionaries and lists
    # if 'messages' in transaction_results:
    #     results['messages'] += transaction_results['messages']
    #
    # card_not_present_results = query_card_not_present(mailbox)
    # if 'messages' in card_not_present_results:
    #     results['messages'] += query_card_not_present(mailbox)['messages']
    return transaction_results


def get_messages(email_type, mailbox):
    if email_type == EmailType.TRANSACTION:
        results = run_financial_email_queries(mailbox)
    elif email_type == EmailType.BALANCE_SUMMARY:
        results = query_balance_summary_alert(mailbox)
    else:
        results = {}
    return results


# Query the email type
# Loop through all relevant messages
# Run the appropriate handler for the email messages
# Mark the email message as read so it cannot be queried again the next time the app runs
def handle_mail_request(email_type):
    try:
        mailbox = MailBox(MAIL_IMAP_HOST).login(MAIL_IMAP_USERNAME, MAIL_IMAP_PASSWORD, TRANSACTION_LABEL)
        messages = get_messages(email_type, mailbox)

        count = 0
        for message in messages:
            count += 1
            email_fields = parse_email_message(message)
            handle_email_message(email_type, email_fields)
            mailbox.flag(message.uid, imap_tools.MailMessageFlags.SEEN, True)
        print(f"There were {count} emails")
    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        logger.error(f"An error occurred: {error}")
