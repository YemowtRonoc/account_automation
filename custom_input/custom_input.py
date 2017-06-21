"""
Module to control user input
"""

def input_email(prompt):
    """
    Input that only accepts valid email address
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
    """
    import re
    ip_address = None
    while ip_address is None:
        print prompt
        user_input = raw_input()
        ip_regex = \
        r'''(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}
                ([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'''
        if re.search(ip_regex, user_input, re.X) is not None:
            ip_address = user_input
        else:
            print "The IP Address has the wrong format"

    return ip_address

def input_string(prompt):
    """
    Get user inputted string
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
