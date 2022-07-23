"""Test login on Scotty Cameron site"""

import os
import time

import undetected_chromedriver as uc

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException

    
def main():
    try:
        USERNAME = os.environ['UN']
        PASSWORD = os.environ['PW']

    except KeyError:
        print('Enter env variables!!')
        return 0

    LOGIN_URL = "https://www.scottycameron.com/store/user/login/"

    driver = uc.Chrome()

    driver.get(LOGIN_URL)

    wait = WebDriverWait(driver, 10)
    page_reached = wait.until(ec.url_to_be(LOGIN_URL))

    #USERNAME
    username_input = driver.find_element(By.XPATH, "//input[@id='login_username']")
    username_input.send_keys(USERNAME)

    password_input = driver.find_element(By.XPATH, "//input[@id='login_password']")
    password_input.send_keys(PASSWORD)

    login_button = driver.find_element(By.XPATH, "//button[@id='loginButton']")
    login_button.click()

    time.sleep(45)


if __name__ == "__main__":
    main()




