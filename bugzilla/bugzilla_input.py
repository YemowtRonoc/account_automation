"""
Module to get user input for bugzilla automation values
"""
import getpass

import bugzilla_automation
from custom_input.custom_input import input_email
import constants

def input_admin_bugzilla_credentials(admin_credentials):
    """
    Retrieve admin credentials for bugzilla
    """
    if admin_credentials['Bugzilla_login'] is None:
        admin_credentials['Bugzilla_login'] = input_email("What is the admin email address?")

    if admin_credentials['Bugzilla_password'] is None:
        while admin_credentials['Bugzilla_password'] is None:
            print "What is the admin password?"
            user_input = getpass.getpass()
            if len(user_input) <= 0:
                print "Please enter a valid password."
            else:
                admin_credentials['Bugzilla_password'] = user_input

    return admin_credentials

def begin_automation(user_credentials, admin_credentials):
    """
    Begin's automation process
    """
    status = False
    while status is False:
        admin_credentials = input_admin_bugzilla_credentials(admin_credentials)
        status = bugzilla_automation.create_user_in_bugzilla( \
                        constants.BUGZILLA_URL, user_credentials, admin_credentials)
