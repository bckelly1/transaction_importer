import logging
import os

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

TOKEN_FILE_NAME = 'credentials/token.json'
CREDENTIALS_FILE_NAME = 'credentials/credentials.json'

# If modifying these scopes, delete the file token.json.
# Need:
#   readonly for reading emails
#   modify to adjust the labels (Mark as read)
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.modify']

logger = logging.getLogger('google_credentials')


# TODO: Find a better way to do this. This is the most infuriating way to do this. This token invalidates itself every 7
#   Days until the app is published. I don't really want to publish this app, I just want to talk to the API to get my
#   Emails. Instead I have to re-validate the auth token by hand every 7 days.
def revalidate_creds(creds):
    if creds and creds.expired and creds.refresh_token:
        logging.info('Gmail token was expired. Refreshing...')
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE_NAME, SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open(TOKEN_FILE_NAME, 'w') as token:
        token.write(creds.to_json())
    return creds


def get_gmail_creds():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    token_file_name = TOKEN_FILE_NAME
    if os.path.exists(token_file_name):
        creds = Credentials.from_authorized_user_file(token_file_name, SCOPES)
    # If there are no (valid) credentials available, reauthenticate user.
    if not creds or not creds.valid:
        creds = revalidate_creds(creds)
    return creds
