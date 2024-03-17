import logging
import os.path

from logger import *

TRANSACTION_AFTER = os.environ.get('TRANSACTION_AFTER', '2023/12/22')
TRANSACTION_BEFORE = os.environ.get('TRANSACTION_BEFORE', '2023/12/29')

# QUERY_TIMERANGE = f'is:unread after:{TRANSACTION_AFTER} before:{TRANSACTION_BEFORE}'
QUERY_TIMERANGE = f'is:unread'

TRANSACTION_LABEL = os.environ.get('TRANSACTION_LABEL')

logger = logging.getLogger('google_grabber')


# Largely unused. If you need to find the ID of a new label, this function will do it
# name: 'Financial/Transactions'
def find_label_id(service, name):
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        logging.info('No labels found.')
        return
    if name is None:
        logging.info('Labels:')
        for label in labels:
            logging.info(label['name'] + ' ' + label['id'])
    else:
        for label in labels:
            if label['name'] == name:
                return label['id']


def query_mailbox(service, query_string, label):
    return service.users().messages().list(userId='me', labelIds=[label], q=query_string).execute()


# Most useful, gets all transaction across all accounts
def query_transactions(service):
    mail_query = f'"Transaction" {QUERY_TIMERANGE}'
    return query_mailbox(service, mail_query, TRANSACTION_LABEL)


def query_card_not_present(service):
    mail_query = f'"Card Not Present" {QUERY_TIMERANGE}'
    return query_mailbox(service, mail_query, TRANSACTION_LABEL)


# Summary Queries
def query_daily_balance(service):
    mail_query = f'"Daily Balance" {QUERY_TIMERANGE}'
    return query_mailbox(service, mail_query, TRANSACTION_LABEL)


def query_position_summary(service):
    mail_query = f'"Position Summary" {QUERY_TIMERANGE}'
    return query_mailbox(service, mail_query, TRANSACTION_LABEL)


def query_account_summary(service):
    mail_query = f'"Account Summary" {QUERY_TIMERANGE}'
    return query_mailbox(service, mail_query, TRANSACTION_LABEL)


def query_balance_summary_alert(service):
    mail_query = f'"Balance Summary Alert" {QUERY_TIMERANGE}'
    return query_mailbox(service, mail_query, TRANSACTION_LABEL)


# Debit transactions
def query_deposit_received(service):
    mail_query = f'"Deposit Received" {QUERY_TIMERANGE}'
    return query_mailbox(service, mail_query, TRANSACTION_LABEL)


def query_credit_card_debit_posted(service):
    mail_query = f'"Credit Card Debit Posted" {QUERY_TIMERANGE}'
    return query_mailbox(service, mail_query, TRANSACTION_LABEL)
