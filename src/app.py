from controller import *
from logger import *


@app.route('/')
def hello():
    return base_page()


@app.route('/run-transaction-import')
def run_main_import():
    entrypoint(EmailType.TRANSACTION)
    return 'Success!'


@app.route('/run-balance-summary-import')
def run_balance_summary_import():
    entrypoint(EmailType.BALANCE_SUMMARY)
    return 'Success!'


if __name__ == '__main__':
    app.logger.info(f'Running in {os.getcwd()}')
    app.run(host='0.0.0.0', port=5010)
