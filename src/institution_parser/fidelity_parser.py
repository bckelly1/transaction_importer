import logging

logger = logging.getLogger('fidelity_parser')


# Given an array of words, find the first one that contains a money value; $12.34
def find_money_value(description_tokens):
    for word in description_tokens:
        if '$' in word:
            return word


# Fidelity is super annoying. The actual body of the message isn't structured well at all.
# International transactions have a slightly different email template and has to be parsed differently.
def handle_fidelity_card_transaction(text, headers):
    lines = text.split("\n")
    card_number = lines[0].split(' ')[-1].strip()
    original_description = lines[1].split('. ')[0].strip()
    tokens = original_description.strip().split(' ')
    amount = float(find_money_value(tokens).replace('$', ''))  # TODO: Not super proud of this
    merchant_tokens = []
    for n in range(tokens.index('at') + 1, len(tokens)):  # TODO: Not super proud of this either
        merchant_tokens.append(tokens[n])
    merchant = ' '.join(merchant_tokens)

    logger.info('Card Number: ' + card_number)
    logger.info('amount: ' + str(amount))
    logger.info('detail: ' + original_description + "\n")
    return \
        [{
            'date': headers['Date'],
            'description': merchant,
            'original_description': original_description,
            'amount': amount,
            'transaction_type': 'debit',
            'category': '',
            'merchant': merchant,
            'account_number': card_number,
            'notes': 'Fidelity'
        }]
