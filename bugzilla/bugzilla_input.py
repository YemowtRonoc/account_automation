"""
Module to get user input for bugzilla automation values
"""
import getpass

import bugzilla_automation
from custom_input.custom_input import input_email

def input_admin_bugzilla_credentials(admin_credentials):
    """
    Retrieve admin credentials for bugzilla
    
    Bugzilla_login and Bugzilla password are named to fit the html
    tag ids of the input fields. It can be changed easily but will
    require a change in bugzilla_automation.sign_in() to keep the program
    working

    admin_credentials is passed as some of the credentials may have been 
    created using cli arguments.
    """
    if admin_credentials['Bugzilla_login'] is None:
        admin_credentials['Bugzilla_login'] = input_email("What is the admin email address?")

    if admin_credentials['Bugzilla_password'] is None:
        while admin_credentials['Bugzilla_password'] is None:
            print "What is the admin password for bugzilla?"
            user_input = getpass.getpass()
            if len(user_input) <= 0:
                print "Please enter a valid password."
            else:
                admin_credentials['Bugzilla_password'] = user_input

    return admin_credentials
