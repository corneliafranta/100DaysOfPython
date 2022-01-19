from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = 'C:\Development\chromedriver.exe'
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://python.org')
event_details = []
event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time ')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget .menu a')
for index in range(0, len(event_names)):
    object = {
        'time': event_times[index].text,
        'name': event_names[index].text
    }
    event_details.append(object)

print(event_details)

driver.quit()