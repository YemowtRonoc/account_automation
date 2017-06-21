"""
Module to create email before sending through gmail.
"""
import os
import oauth2client
from oauth2client import client
from oauth2client import tools
from httplib2 import Http

import gmail_api

FLAGS = None

SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = './account_automation/client_secret.json'
APPLICATION_NAME = 'Gmail API Quickstart'
EMAIL_SUBJECT = "Welcome to <<company-name>>"
EMAIL_TEXT = """Hi %s,

Welcome to <<company-name>>. 
We have set you up with some accounts automatically.
This email will explain what the various accounts do.

Ask me for your default password when you are ready.
I'd also recommend that you change your passwords as soon as possible.

Bugzilla:
This is our issue tracking system. 
To sign in, use your email address and password which we set up for you.
Check the documentation link below if you haven't used it before,
and ask someone in the office if you have any questions.

Bugzilla Home: <<bugzilla-url>>
Some documentation: https://www.bugzilla.org/docs/3.0/html/using.html


Repo Server:
This is how you can clone the repos for the various things you could be working on. 
If you're not a developer then you won't have the necessary permissions to push
to the git repos, but you won't need that anyway.

To access the repo server you need to ssh, with your initials in lowercase as the username
to '<<git-server>>'. So, you would be typing: "ssh fs@<<git-server>>", assuming your name is Forename Surname. 
You will be prompted for your password which can be retrieved from myself verbally.

    Cloning:
    To clone the git repos, go to where you would like to hold your local copy. 
    Enter the command: "git clone fs@<<git-server>>:/home/git/repos/<project>"
    This will checkout that repo where you are.


To gain access to a build VM, you will need to talk to the build engineer 
(currently <<build-engineer>>). They will set you up and tell you how to use it.

You will need access to a build VM for the following:

To build a basic distribution, follow the tutorial link below
Wiki:http://<<wiki-server>>:8082/mediawiki/<<build-tutorial>>


Other important links can be found here: http://<<wiki-server>>/


This message was automatically generated."""


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

    email_text = EMAIL_TEXT % (user_name)
    message = gmail_api.create_message(admin_email, user_email, \
                                EMAIL_SUBJECT, email_text)
    gmail_api.send_message(service, admin_email, message)
