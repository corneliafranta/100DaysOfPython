import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

DRIVER_PATH = 'C:\Development\chromedriver.exe'
FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLSeUsUKorrEAIYy4pVBekf_NoKJZ1Sb5di-AHGpUU9ODsGh9PQ/viewform?usp=sf_link'
IMMO_LINK = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'

HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Accept-Language': 'de-DE,de;q=0.9,en;q=0.8,sv;q=0.7'
}

service = Service(DRIVER_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


def get_data():
    response = requests.get(IMMO_LINK, headers=HEADER)

    contents = response.text

    soup = BeautifulSoup(contents, 'html.parser')

    links = [f"https://www.zillow.com{link['href']}" for link in soup.find_all(name='a', class_="list-card-link")]
    prices = [link.text.split()[0][1:-1] for link in soup.find_all(name='div', class_="list-card-price")]
    addresses = [address.text for address in soup.find_all(name="address")]

    return [links, prices, addresses]
data = get_data()
print(data)
def fill_in_form(link, price, address):

    input_1 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_2 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_3 = driver.find_element(By.XPATH,
                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_1.send_keys(address)
    input_2.send_keys(price)
    input_3.send_keys(link)
    submit_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_btn.click()
    time.sleep(2)
    next_btn = driver.find_element(By.LINK_TEXT, 'Weitere Antwort senden')
    next_btn.click()
    time.sleep(1)

def sign_in():
    sign_in_btn = driver.find_element(By.LINK_TEXT, 'In Google anmelden')
    sign_in_btn.click()
    email_input = driver.find_element(By.NAME, 'identifier')
    email_input.send_keys('corneliadevarennes@gmail.com')
    continue_btn = driver.find_element(By.CLASS_NAME, 'VfPpkd-vQzf8d')
    continue_btn.click()


driver.get(FORM_LINK)
sign_in()
#for index in range(len(data[0])):
#    fill_in_form(data[0][index], data[1][index], data[2][index])
