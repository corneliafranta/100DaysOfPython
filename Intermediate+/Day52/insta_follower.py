import os
import time

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = 'C:\Development\chromedriver.exe'
SIMILAR_ACCOUNT = 'vegan'
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')


class InstFollower:
    def __init__(self):
        self.driver = self.create_driver()

    @staticmethod
    def create_driver():
        service = Service(CHROME_DRIVER_PATH)
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def open_page(self):
        self.driver.get('https://www.instagram.com/')

    def login(self):
        self.accept_cookies()
        time.sleep(5)
        username_input = self.driver.find_element(By.NAME, 'username')
        password_input = self.driver.find_element(By.NAME, 'password')
        sign_in_btn = self.driver.find_element(By.CSS_SELECTOR, 'form button')
        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)
        sign_in_btn.click()
        time.sleep(5)
        not_now_btn = self.driver.find_element(By.CLASS_NAME, 'HoLwm')
        not_now_btn.click()
        time.sleep(5)

    def accept_cookies(self):
        accept_btn =self.driver.find_element(By.CLASS_NAME, 'bIiDR')
        accept_btn.click()

    def find_followers(self):
        search_input = self.driver.find_element(By.CSS_SELECTOR, '.P0xOK input')
        search_input.send_keys(SIMILAR_ACCOUNT)
        time.sleep(3)
        page = self.driver.find_element(By.CSS_SELECTOR, '.fuqBx a')
        page.click()
        time.sleep(5)
        show_followers_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        show_followers_btn.click()
        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()





