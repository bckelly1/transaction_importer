import imap_tools
from imap_tools import MailBox, A

import logging
import os.path

from logger import *

TRANSACTION_AFTER = os.environ.get('TRANSACTION_AFTER', '2023/12/22')
TRANSACTION_BEFORE = os.environ.get('TRANSACTION_BEFORE', '2023/12/29')

# QUERY_TIMERANGE = f'is:unread after:{TRANSACTION_AFTER} before:{TRANSACTION_BEFORE}'
QUERY_TIMERANGE = f'is:unread'

MAIL_IMAP_HOST = os.environ.get('MAIL_IMAP_HOST')
MAIL_IMAP_USERNAME = os.environ.get('MAIL_IMAP_USERNAME')
MAIL_IMAP_PASSWORD = os.environ.get('MAIL_IMAP_PASSWORD')
TRANSACTION_LABEL = os.environ.get('TRANSACTION_LABEL', 'INBOX')

logger = logging.getLogger('google_grabber')


def query_mailbox(mailbox, mail_query='*'):

    results = mailbox.fetch(A(subject=mail_query, seen=False), mark_seen=False)
    # for result in results:
    #     print(result)

    return results
# query_mailbox(mailbox)

# Most useful, gets all transaction across all accounts
def query_transactions(mailbox):
    mail_query = 'Transaction'
    return query_mailbox(mailbox, mail_query=mail_query)


def query_card_not_present(mailbox):
    mail_query = f'"Card Not Present" {QUERY_TIMERANGE}'
    return query_mailbox(mailbox, mail_query)


# Summary Queries
def query_daily_balance(mailbox):
    mail_query = f'"Daily Balance" {QUERY_TIMERANGE}'
    return query_mailbox(mailbox, mail_query)


def query_position_summary(mailbox):
    mail_query = f'"Position Summary" {QUERY_TIMERANGE}'
    return query_mailbox(mailbox, mail_query)


def query_account_summary(mailbox):
    mail_query = f'"Account Summary" {QUERY_TIMERANGE}'
    return query_mailbox(mailbox, mail_query)


def query_balance_summary_alert(mailbox):
    mail_query = f'"Balance Summary Alert" {QUERY_TIMERANGE}'
    return query_mailbox(mailbox, mail_query)


# Debit transactions
def query_deposit_received(mailbox):
    mail_query = f'"Deposit Received" {QUERY_TIMERANGE}'
    return query_mailbox(mailbox, mail_query)


def query_credit_card_debit_posted(mailbox):
    mail_query = f'"Credit Card Debit Posted" {QUERY_TIMERANGE}'
    return query_mailbox(mailbox, mail_query)
