"""
Module to get admin credentials for ssh automation
"""
import getpass
import subprocess
import os

from custom_input.custom_input import input_ip_address
from custom_input.custom_input import input_string
import constants

def input_admin_ssh_credentials(ssh_credentials):
    """
    Retrieve admin credentials as user input
    """
    if ssh_credentials['ip_address'] is None:
        ssh_credentials['ip_address'] = input_ip_address( \
                            "What is the IP address of the repo server?")

    if ssh_credentials['name'] is None:
        ssh_credentials['name'] = input_string( \
                "What is the admin username on the repo server? (%s)" % \
                                             ssh_credentials['ip_address'])

    if ssh_credentials['password'] is None:
        while ssh_credentials['password'] is None:
            print "What is the admin password for the repo server?"
            user_input = getpass.getpass()
            if len(user_input) <= 0:
                print "Please enter a valid password"
            else:
                ssh_credentials['password'] = user_input

    return ssh_credentials

def shell_script(admin_credentials, user_credentials):
    """
    Starts shell script and runs it through to add user to system
    """
    script_str = "bash %s \"%s\" \"%s\" \"%s\" \"%s\" \"%s\"" % \
            (constants.SCRIPT_NAME, admin_credentials['name'], \
            admin_credentials['password'], admin_credentials['ip_address'], \
            user_credentials['name'].lower(), user_credentials['dev'])

    subprocess.call(script_str, shell=True)

def begin_automation(user_credentials):
    """
    Begins automation process for repo server account
    """
    ssh_credentials = {}
    ssh_credentials = input_admin_ssh_credentials(ssh_credentials)
    shell_script(ssh_credentials, user_credentials)

if __name__ == "__main__":
    SSH_CREDENTIALS = {}
    SSH_CREDENTIALS = input_admin_ssh_credentials(SSH_CREDENTIALS)
    shell_script(SSH_CREDENTIALS, constants.USER_CREDENTIALS)
