from selenium import webdriver
from selenium.webdriver.chrome.service import Service



chrome_driver_path ='C:\Development\chromedriver.exe'
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.amazon.com')
# driver.close() => Closes particular Tab
driver.quit() # Closes whole browser