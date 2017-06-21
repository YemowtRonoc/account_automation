"""
Initialisation module for accounts automation
"""
import argparse

import bugzilla.bugzilla_input as bugzilla_input
import bugzilla.bugzilla_automation as bugzilla_automation
import constants
import ssh_repos.ssh_input as ssh_input
from custom_input.custom_input import input_email
from custom_input.custom_input import input_string
from email_notification.create_email import create_email

def input_user_details(user_details):
    """
    Retrieve user details to create bugzilla account.
    """
    if user_details['name'] is None:
        user_details['name'] = input_string("What is the new user's name?")

    if user_details['login'] is None:
        user_details['login'] = input_email("What is the new user's email address?")

    if user_details['dev'] is None:
        while user_details['dev'] is None:
            print "Is the new user a developer? (yes/no)"
            user_input = raw_input()
            if user_input:      #Python sequences evaluate to False when empty
                user_input = user_input.lower()
                if user_input == 'y' or user_input == 'yes':
                    user_details['dev'] = True
                elif user_input == 'n' or user_input == 'no':
                    user_details['dev'] = False

    user_details['password'] = constants.DEFAULT_PASSWORD

    return user_details



def main():
    """
    Main function, entry point for account automation program.
    """
    user_details = {'name':None, 'login':None, 'password':None, 'dev':None}
    bugzilla_credentials = {'Bugzilla_login':None, 'Bugzilla_password':None}
    ssh_credentials = {'name':None, 'password':None, 'ip_address':None}

    parser = argparse.ArgumentParser(description=\
                "This automates creation of bugzilla and repo(git) accounts")

    parser.add_argument("-n", "--name", help="Name of the new hire")
    parser.add_argument("-e", "--email", help="Email of the new hire")
    # parser.add_argument("-p", "--position", help="Position of the new hire")
    parser.add_argument("-d", "--dev", action="store_true", \
                            help="If the new user is a developer, add this.")
    parser.add_argument("-a", "--adminemail", \
                                        help="Email address for the automator")
    parser.add_argument("-r", "--reposerver", \
                        help="Repo Server domain (e.g. ssh fs@<--reposerver>)")
    parser.add_argument("-u", "--adminusername", \
                                        help="Admin username on repo server")

    args = parser.parse_args()

    if args.name:
        user_details['name'] = args.name
    if args.email:
        user_details['login'] = args.email
    # if args.position:
    #     user_details['position'] = args.position
    if args.dev:
        user_details['dev'] = True
    if args.adminemail:
        bugzilla_credentials['Bugzilla_login'] = args.adminemail
    if args.reposerver:
        ssh_credentials['ip_address'] = args.reposerver
    if args.adminusername:
        ssh_credentials['name'] = args.adminusername

    print "Please ensure you have ssh keys set up with the repo server."

    user_details = input_user_details(user_details)
    print """
==========================
    Bugzilla (%s)
==========================
    """ % (constants.BUGZILLA_URL, )
    bugzilla_credentials = bugzilla_input.input_admin_bugzilla_credentials(\
                                                        bugzilla_credentials)

    print """
========================
    Repo Server
========================
    """
    ssh_credentials = ssh_input.input_admin_ssh_credentials(ssh_credentials)

    print """
========================
    Working now...
========================
    """

    bugzilla_automation.create_user_in_bugzilla(constants.BUGZILLA_URL, \
                                        user_details, bugzilla_credentials)
    ssh_input.shell_script(ssh_credentials, user_details)
    create_email(user_details['login'], bugzilla_credentials['Bugzilla_login'], \
                            user_details['name'])

if __name__ == "__main__":
    main()
