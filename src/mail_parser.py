import base64
import datetime
import logging

from enum import Enum
from institution_parser.first_tech_parser import *
from institution_parser.fidelity_parser import *
from institution_parser.us_bank_parser import *


logger = logging.getLogger('fidelity_parser')


class Institution(Enum):
    FIDELITY = 'Fidelity'
    FIRST_TECH = 'First Tech'
    HOME_DEPOT = 'Home Depot'
    US_BANK = 'US Bank'


def determine_institution(text):
    if 'Fidelity' in text:
        return Institution.FIDELITY
    elif 'First Tech' in text:
        return Institution.FIRST_TECH
    elif 'Home Depot' in text:
        return Institution.HOME_DEPOT
    elif 'U.S. Bank' in text or 'King Soopers' in text or 'Kroger' in text:
        return Institution.US_BANK
    else:
        return None


def parse_headers(headers):
    parsed_headers = {}
    for header in headers:
        parsed_headers[header['name']] = header['value']
    return parsed_headers


def parse_message_text(part):
    text = None
    try:
        email_data = part['body']['data']
        byte_code = base64.urlsafe_b64decode(email_data)

        text = byte_code.decode('utf-8')
    except BaseException as error:
        logger.error(f"An error occurred: {error}")
    return str(text)


def parse_email_message(msg):
    payload = msg['payload']
    headers = parse_headers(payload['headers'])  # Could pick out from the title if it's an email we know how to parse
    from_name = headers['From']
    subject = headers['Subject']
    try:
        # Extract the Epoch whenever possible. There are ~6 date fields, only trust the one from the mail server
        epoch = int(headers['ARC-Seal'].split('; ')[2].split('=')[1])
        date = datetime.datetime.fromtimestamp(epoch)
        headers['Date'] = date
    except ValueError:
        logger.error('Could not parse date as standard format.')

    # No idea why they added that, should be removed
    headers['Message-ID'] = headers['Message-ID'].replace('>', '').replace('<', '').replace('-', '')
    message_id = headers['Message-ID']

    if 'parts' in payload.keys():
        # Not sure if I need to take apart the other parts, the first part appears to have the plain text
        text = parse_message_text(payload['parts'][0])
    else:
        text = parse_message_text(payload)
    if 'gas station' in text in text:
        # These are usually duplicate messages, can be ignored
        return
    result = {
        'payload': payload,
        'headers': headers,
        'from_name': from_name,
        'subject': subject,
        'message_id': message_id,
        'text': text
    }
    return result


def extract_transactions(email_fields):
    institution = determine_institution(email_fields['from_name'])
    if institution == Institution.FIDELITY and 'Transaction' in email_fields['subject']:
        transactions = handle_fidelity_card_transaction(email_fields['text'], email_fields['headers'])
    elif institution == Institution.FIRST_TECH and 'Transaction' in email_fields['subject']:
        transactions = handle_first_tech_transaction(email_fields['text'], email_fields['headers'])
    elif institution == Institution.US_BANK and 'transaction' in email_fields['subject']:
        transactions = handle_us_bank_transaction(email_fields['text'], email_fields['headers'])
    else:
        transactions = []  # Placeholder for future types
    return transactions


def extract_accounts(email_fields):
    institution = determine_institution(email_fields['from_name'])
    if institution == Institution.FIDELITY:
        raise Exception("Fidelity is not implemented yet")
    elif institution == Institution.FIRST_TECH:
        return handle_first_tech_balance_summary(email_fields['text'])
