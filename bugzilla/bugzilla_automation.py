"""
Module to automate bugzilla account creation
"""
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

BUGZILLA_LOGOUT_URL_EXTENSION = 'index.cgi?logout=1'
BUGZILLA_ADD_USER_URL_EXTENSION = 'editusers.cgi?action=add'
SELENIUM_DELAY = 3.5          #Seconds

def fill_elements(driver, dictionary):
    """
    Fill elements on page using dictionary of
    fields and values (as keys and values respectively)

    driver: Selenium web driver, used to fill information.
    dictionary: list of element with the key as the field html
        id tag, and the value as the input value to be filled in.
    """
    for key, value in dictionary.items():
        try:
            elem = driver.find_element_by_name(key)
            elem.clear()
            elem.send_keys(value)
        except NoSuchElementException:
            print "EXCEPTION: Element with name '%s' not found on page" % key

def sign_in(driver, admin_credentials):
    """
    Signs into bugzilla.

    driver: Selenium web driver, used to fill in information.
    admin_credentials: dict of details required to log in.
    """
    fill_elements(driver, admin_credentials)

    elem = driver.find_element_by_name("GoAheadAndLogIn")
    elem.click()

def create_user_in_bugzilla(bugzilla_url, user_values, admin_credentials):
    """
    Opens bugzilla in firefox. Signs in and adds new user account.
    url: bugzilla url to add user.
    user_values: dictionary with keys as field names, and values as field values.
    """
    created_user = False

    driver = webdriver.Firefox()

    url = "%s%s" % (bugzilla_url, (BUGZILLA_ADD_USER_URL_EXTENSION))
    driver.get(url)
    sign_in(driver, admin_credentials)

    time.sleep(SELENIUM_DELAY)

    try:
        driver.find_element_by_id('notify_user')
        fill_elements(driver, user_values)

        elem = driver.find_element_by_id("add")
        elem.click()

        time.sleep(SELENIUM_DELAY)
        created_user = True
    except NoSuchElementException as exc:
        print exc
        print "Invalid admin credentials, could not sign in"

    url = "%s%s" % (bugzilla_url, (BUGZILLA_LOGOUT_URL_EXTENSION))
    driver.get(url)

    time.sleep(SELENIUM_DELAY)
    driver.close()

    return created_user
