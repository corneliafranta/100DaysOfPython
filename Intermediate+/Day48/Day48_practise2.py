from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path ='C:\Development\chromedriver.exe'
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://python.org')
#price = driver.find_element(By.CLASS_NAME, 'a-price')
#print(price.text)
# driver.close() => Closes particular Tab

element = driver.find_element(By.NAME, 'q')
print(element.tag_name)

logo = driver.find_element(By.CLASS_NAME, 'python-logo')
print(logo.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a')
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)





driver.quit()