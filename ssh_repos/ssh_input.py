"""
Module to get admin credentials for ssh automation
"""
import getpass
import subprocess

from custom_input.custom_input import input_ip_address
from custom_input.custom_input import input_string

USER_CREDENTIALS = {'login':'conor.twomey@<<company-name>>.com', 'dev':True, \
                            'name':'Conor Twomey', 'password':'hello123'}
SCRIPT_NAME = './ssh_repos/add_user_ssh.sh'

def input_admin_ssh_credentials(ssh_credentials):
    """
    Retrieve admin credentials as user input
    ssh_credentials: dict of admin ssh credentials for logging in
    """
    if ssh_credentials['ip_address'] is None:
        ssh_credentials['ip_address'] = input_ip_address( \
                            "What is the IP address of the repo server?")

    if ssh_credentials['name'] is None:
        ssh_credentials['name'] = input_string( \
                "What is the admin username on the repo server? (%s)" % \
                                             ssh_credentials['ip_address'])

    if ssh_credentials['password'] is None and \
            (ssh_credentials['name'] != 'root' or ssh_credentials['key'] == False):
        while ssh_credentials['password'] is None:
            print "What is the admin password for the repo server?"
            user_input = getpass.getpass()
            if len(user_input) <= 0:
                print "Please enter a valid password"
            else:
                ssh_credentials['password'] = user_input

    return ssh_credentials

def shell_script(ssh_credentials, user_credentials):
    """
    Starts shell script and runs it through to add user to system
    ssh_credentials: dict used for expect scripts to sign into ssh 
        and perform necessary tasks
    user_credentials: dict used for expect scripts to create user
        accounts on repo server
    """
    script_str = "bash %s \"%s\" \"%s\" \"%s\" \"%s\" \"%s\"" % \
            (SCRIPT_NAME, ssh_credentials['name'], \
            ssh_credentials['password'], ssh_credentials['ip_address'], \
            user_credentials['name'].lower(), user_credentials['dev'])

    subprocess.call(script_str, shell=True)

def begin_automation(user_credentials):
    """
    Begins automation process for repo server account
    user_credentials: dict of user details used later for expect scripts
        of account creation for the repo server
    """
    ssh_credentials = {}
    ssh_credentials = input_admin_ssh_credentials(ssh_credentials)
    shell_script(ssh_credentials, user_credentials)
