"""Test login on Scotty Cameron site"""

import os
import time
import getpass

import undetected_chromedriver as uc

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException

    
def login_user(username, password):
    LOGIN_URL = "https://www.scottycameron.com/store/user/login/"

    driver = uc.Chrome()

    driver.get(LOGIN_URL)

    wait = WebDriverWait(driver, 10)
    page_reached = wait.until(ec.url_to_be(LOGIN_URL))

    username_input = driver.find_element(By.XPATH, "//input[@id='login_username']")
    username_input.send_keys(username)

    password_input = driver.find_element(By.XPATH, "//input[@id='login_password']")
    password_input.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[@id='loginButton']")
    login_button.click()

    print("Sleeping for 20 seconds...")
    time.sleep(20)
    print("Sleep exited")


if __name__ == "__main__":
    UN = input("Please enter your username:")
    PW = getpass.getpass("Please enter your password:")

    login_user(UN, PW)
