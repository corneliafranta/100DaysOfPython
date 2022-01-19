from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_dirver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_dirver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

num_articles = driver.find_element(By.CSS_SELECTOR, '#articlecount a').text

print(num_articles)

driver.quit()

