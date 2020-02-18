from selenium import webdriver
import selenium.common.exceptions as seleniumError
from selenium.webdriver.common.keys import Keys
import http.client
import time


def yahoo(user, password, minutes=3):
    """Accepts 3 arguments:
    Username - Username for Yahoo Account
    Password - Password for Yahoo Account
    minutes - optional - minutes for program to run

    This program will delete large batches of emails in inbox of Yahoo account with zero discrimination.
    Use with caution.
    """

    entries = []
    elements = ['login-username','password']
    counter = 0

    entries.append(user)
    entries.append(password)
    # TODO Exception Handling for webdriver
    browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    # TODO Exception handling for browser. Known exceptions: RemoteDisconnected
    # Time program will wait for applicable web elements to appear - in seconds
    browser.implicitly_wait(10)
    browser.get('https://login.yahoo.com/config/login?.src=fpctx&.intl=us&.lang=en-US&.done=https://www.yahoo.com')
    count = 0
    element = elements[0]
    # TODO Exception handling for element. Known exception: NoSuchElementException
    elem = browser.find_element_by_id(element)
    elem.send_keys(entries[count])
    elem.send_keys(Keys.ENTER)

    # Password Field
    element = elements[1]
    counter = 0
    # while counter < 3:
    #     counter += 1
    #     try:
    #         browser.get(browser.current_url)
    #     except http.client.RemoteDisconnected:
    #         print('Password Connection Fail')
    #
    #     else:
    #
    #         break;
    # TODO Exception Handling: Nosuchelement, Remotedisconnected?
    elem = browser.find_element_by_name(element)
    count += 1
    elem.send_keys(entries[count])
    # elem.submit()
    elem.send_keys(Keys.ENTER)

    # Yahoo Mail
    counter = 0
    while counter < 3:
        try:
            browser.get('https://mail.yahoo.com/?.src=fp')
        except http.client.RemoteDisconnected:
            print('Connection Failed. Trying again...')
            #TODO Breaking loop if 3 attempts
        else:
            # TODO: Add remaining code instead of break
            break;

    checkboxcssselector = '[data-test-id="checkbox"]'
    try:
        # Checkbox for Select All Emails
        elem = browser.find_element_by_css_selector(checkboxcssselector)
    except seleniumError.NoSuchElementException:
        print('Checkbox Not Found. Either due to Invalid Credentials or No Emails in Inbox. Closing Program...')
    else:
        endTime = time.time() + 60 * minutes
        while time.time() < endTime:
            try:
                elem.click()
                elem.send_keys(Keys.DELETE)
            except seleniumError.ElementClickInterceptedException:
                print('Waiting on Checkbox to reappear...')


