from imap_tools import A

import logging
import os.path

from logger import *

MAIL_IMAP_HOST = os.environ.get('MAIL_IMAP_HOST')
MAIL_IMAP_USERNAME = os.environ.get('MAIL_IMAP_USERNAME')
MAIL_IMAP_PASSWORD = os.environ.get('MAIL_IMAP_PASSWORD')
TRANSACTION_LABEL = os.environ.get('TRANSACTION_LABEL', 'INBOX')

logger = logging.getLogger('mail_fetcher')


def query_mailbox(mailbox, mail_query='*'):
    results = mailbox.fetch(A(subject=mail_query, seen=False), mark_seen=False)
    return results


# Most useful, gets all transaction across all accounts
def query_transactions(mailbox):
    mail_query = 'Transaction'
    return query_mailbox(mailbox, mail_query=mail_query)


def query_card_not_present(mailbox):
    mail_query = 'Card Not Present'
    return query_mailbox(mailbox, mail_query)


# Summary Queries
def query_daily_balance(mailbox):
    mail_query = 'Daily Balance'
    return query_mailbox(mailbox, mail_query)


def query_position_summary(mailbox):
    mail_query = 'Position Summary'
    return query_mailbox(mailbox, mail_query)


def query_account_summary(mailbox):
    mail_query = 'Account Summary'
    return query_mailbox(mailbox, mail_query)


def query_balance_summary_alert(mailbox):
    mail_query = 'Balance Summary Alert'
    return query_mailbox(mailbox, mail_query)


# Debit transactions
def query_deposit_received(mailbox):
    mail_query = 'Deposit Received'
    return query_mailbox(mailbox, mail_query)


def query_credit_card_debit_posted(mailbox):
    mail_query = 'Credit Card Debit Posted'
    return query_mailbox(mailbox, mail_query)
