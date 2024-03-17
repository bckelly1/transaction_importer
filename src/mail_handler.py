import logging

from database import *
from file_operations import *
from google_grabber import *
from google_credentials import *
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
    time_string = datetime.datetime.strftime(email_fields['headers']['Date'], "%m/%d/%Y, %H:%M:%S")
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


def run_financial_email_queries():
    results = {'messages': []}
    transaction_results = query_transactions()

    # TODO: Feels kinda hacky I just want to merge the dictionaries and lists
    if 'messages' in transaction_results:
        results['messages'] += transaction_results['messages']

    card_not_present_results = query_card_not_present()
    if 'messages' in card_not_present_results:
        results['messages'] += query_card_not_present()['messages']
    return results


def get_messages(email_type, service):
    if email_type == EmailType.TRANSACTION:
        results = run_financial_email_queries()
    elif email_type == EmailType.BALANCE_SUMMARY:
        results = query_balance_summary_alert()
    else:
        results = {}
    return results


# Query the email type
# Loop through all relevant messages
# Run the appropriate handler for the email messages
# Mark the email message as read so it cannot be queried again the next time the app runs
def handle_mail_request(email_type):
    creds = get_gmail_creds()
    try:
        service = build('gmail', 'v1', credentials=creds)
        results = get_messages(email_type, service)
        messages = results.get('messages', [])
        if not messages:
            logger.info('No new messages.')
            return
        logger.info(f"Found {len(messages)} messages")
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            email_fields = parse_email_message(msg)
            handle_email_message(email_type, email_fields)
            service.users().messages().modify(userId='me', id=msg['id'], body={'removeLabelIds': ['UNREAD']}).execute()

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        logger.error(f"An error occurred: {error}")
