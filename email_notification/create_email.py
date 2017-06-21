"""
Module to create email before sending through gmail.
"""
import os
import oauth2client
from oauth2client import client
from oauth2client import tools
from httplib2 import Http

import gmail_api
import constants


FLAGS = None

SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = './account_automation/client_secret.json'
APPLICATION_NAME = 'Gmail API Quickstart'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if FLAGS:
            credentials = tools.run_flow(flow, store, FLAGS)
        else: # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print 'Storing credentials to ' + credential_path
    return credentials

def create_email(user_email, admin_email, user_name):
    """
    Create and pass email to mail API
    """
    from apiclient.discovery import build
    credentials = get_credentials()
    service = build('gmail', 'v1', http=credentials.authorize(Http()))

    email_text = constants.EMAIL_TEXT % (user_name)
    message = gmail_api.create_message(admin_email, user_email, \
                                constants.EMAIL_SUBJECT, email_text)
    gmail_api.send_message(service, admin_email, message)
