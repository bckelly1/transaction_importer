import logging


logger = logging.getLogger('us_bank_parser')


def handle_us_bank_transaction(text, headers):
    lines = text.split("\n")
    original_description = ' '.join(lines[6].split())
    sections = original_description.split('. ')
    short_description = sections[0]
    card_number = sections[1].split(' ')[-1]

    tokens = sections[0].split(' ')
    amount = float(tokens[5].replace('$', ''))
    merchant_tokens = []
    for n in range(7, len(tokens)):
        merchant_tokens.append(tokens[n])
    merchant = ' '.join(merchant_tokens)

    logger.info('Card Number: ' + card_number)
    logger.info('amount: ' + str(amount))
    logger.info('detail: ' + original_description + "\n")
    return \
        [{
            'date': headers['date'],
            'description': short_description,
            'original_description': sections[0] + '. ' + sections[1],
            'amount': amount,
            'transaction_type': 'debit',
            'category': '',  # Should be filled in later by the category inferer
            'merchant': merchant,
            'account_number': card_number,
            'notes': 'US Bank'
        }]
