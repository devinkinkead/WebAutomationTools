from selenium import webdriver
import selenium.common.exceptions as seleniumError
from selenium.webdriver.common.keys import Keys
import urllib3.exceptions as urlError
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

    browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

    # Time program will wait for applicable web elements to appear - in seconds
    browser.implicitly_wait(10)
    browser.get('https://login.yahoo.com/config/login?.src=fpctx&.intl=us&.lang=en-US&.done=https://www.yahoo.com')
    count = 0
    element = elements[0]
    elem = browser.find_element_by_id(element)
    elem.send_keys(entries[count])
    elem.send_keys(Keys.ENTER)

    # Password Field
    element = elements[1]
    counter = 0
    while counter < 3:
        counter += 1
        try:
            browser.get(browser.current_url)
        except http.client.RemoteDisconnected:
            print('Password Connection Fail')
        else:
            break;

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
        else:
            break;

    checkboxcssselector = '.c27KHO0_n.b_0.M_0.i_0.I_T.y_Z2uhb3X.A_6EqO.r_P.C_q.cvhIH6_T.ir3_Z1FS2Mn.P_0'
    try:
        # Checkbox for Select All Emails
        elem = browser.find_element_by_css_selector(checkboxcssselector)
    except seleniumError.NoSuchElementException:
        print('Checkbox Not Found. Likely due to Invalid Credentials. Closing Program...')
    else:
        endTime = time.time() + 60 * minutes
        while time.time() < endTime:
            try:
                elem.click()
                elem.send_keys(Keys.DELETE)
            except seleniumError.ElementClickInterceptedException:
                print('Waiting on Checkbox to reappear...')


