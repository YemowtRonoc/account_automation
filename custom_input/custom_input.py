"""
Module to control user input
"""

def check_valid_ip(input):
    """
    Check's to make sure the input is a valid IPv4 address.
    input: str that should be in IPv4 format
    """
    import re
    result = None
    ip_regex = \
    r'''(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}
            ([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'''
    if re.search(ip_regex, input, re.X) is not None:
        result = True
    else:
        result = False

    return result

def input_email(prompt):
    """
    Input that only accepts valid email address
    prompt: str of prompt for user input for email
    """
    email = None
    while email is None:
        print prompt
        user_input = raw_input()
        if len(user_input) <= 5 and '@' not in user_input and '.' not in user_input:
            print "Please enter a valid email address."
        else:
            email = user_input
    return email

def input_ip_address(prompt):
    """
    Only accept valid IPv4 Addresses
    prompt: str of prompt for user input for ip address
    """
    ip_address = None
    while ip_address is None:
        print prompt
        user_input = raw_input()
        if (check_valid_ip(user_input) == True):
            ip_address = user_input
        else:
            print "Invalid, please enter a valid IP Address"

    return ip_address

def input_string(prompt):
    """
    Get user inputted string
    prompt: str of prompt for user input of string
    """
    result = None
    while result is None:
        print prompt
        user_input = raw_input()
        if len(user_input) >= 0:
            result = user_input
        else:
            print "Invalid, please enter text"

    return result

def input_y_or_n(prompt):
    """
    Get yes or no from user
    prompt: str for user input of yes or no
    """
    result = None
    while result is None:
        print prompt
        user_input = raw_input()
        if len(user_input) > 0:
            user_input = user_input.lower()
            if user_input == 'y' or user_input == 'yes':
                result = True
            elif user_input == 'n' or user_input == 'no':
                result = False
            else:
                print "Invalid, please enter yes(y) or no(n)"

    return result
