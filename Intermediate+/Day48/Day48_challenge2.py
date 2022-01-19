from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://secure-retreat-92358.herokuapp.com')

name_field = driver.find_element(By.NAME, 'fName')
lastname_field = driver.find_element(By.NAME, 'lName')
email_field = driver.find_element(By.NAME, 'email')
sign_up_btn = driver.find_element(By.TAG_NAME, 'button')
name_field.send_keys('Cornelia')
lastname_field.send_keys('Franta')
email_field.send_keys('franta-cornelia@gmx.at')
sign_up_btn.click()



