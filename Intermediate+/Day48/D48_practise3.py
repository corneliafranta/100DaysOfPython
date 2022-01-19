from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "c:\Development\chromedriver.exe"

service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
#article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, 'All portals')

search_bar = driver.find_element(By.NAME, 'search')
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)
