import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


EMAIL = os.environ.get('EMAIL')
PW = os.environ.get('PW')

chrom_webdriver_path = 'C:\Development\chromedriver.exe'

service = Service(chrom_webdriver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&keywords=python&sortBy=R')

try:
    login_btn = driver.find_element(By.LINK_TEXT, 'Einloggen')
except:
    pass
else:
    login_btn.click()
finally:
    un_input = driver.find_element(By.ID, 'username')
    pw_input = driver.find_element(By.ID, 'password')

    un_input.send_keys(EMAIL)
    pw_input.send_keys(PW)

    submit_btn = driver.find_element(By.CSS_SELECTOR, '.login__form_action_container button')
    submit_btn.click()

    time.sleep(3)

    jobs = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')

    for job in jobs:
        print('called')
        job.click()
        time.sleep(2)
        save_btn = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
        save_btn.click()





