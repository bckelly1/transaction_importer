from mail_handler import *
import os

HOSTNAME = os.environ.get('API_HOSTNAME')

# Controller for the main landing page and entrypoint for the application
def entrypoint(email_type):
    handle_mail_request(email_type)


def base_page():  # TODO: Turn these into templates maybe?
    page_text = f"""
    <h1>Hello, World!</h1>
    <a href="{HOSTNAME}/run-transaction-import" class="button">Run Transaction Import</a>
    </br>
    <a href="{HOSTNAME}/run-balance-summary-import" class="button">Run Balance Summary Import</a>
    """
    return page_text
