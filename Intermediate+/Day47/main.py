import smtplib

import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Accept-Language': 'de-DE,de;q=0.9,en;q=0.8,sv;q=0.7'

}
TARGET_PRICE = 100
product_name: str
PRODUCT_URL = 'https://www.amazon.de/Yum-Asia-Mini-Reiskocher-Reiskochfunktionen-Multischooker-Funktionen/dp/B07PQRBT5N/ref=sr_1_2_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=XQ9TTNTLG8B5&keywords=reiskocher&qid=1642502440&refinements=p_76%3A419122031&rnid=419121031&rps=1&sprefix=reiskocher%2Caps%2C86&sr=8-2-spons&psc=1&smid=A1TVB2IWNZK64K&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzOTRaTFhaR1UwTTNVJmVuY3J5cHRlZElkPUEwMTAxOTczMVVSNEtOREM2V1BMRCZlbmNyeXB0ZWRBZElkPUEwMjcwNjgwREg1MUdJVzI3TUFRJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

def get_price():
    global product_name
    response = requests.get(url=PRODUCT_URL, headers= header)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    product_name = soup.find(name='span', id= 'productTitle').getText()
    print(product_name)
    price_whole = soup.find(name='span', class_='a-price-whole').getText()
    price_fraction = soup.find(name='span', class_='a-price-fraction').getText()
    price = float(f"{price_whole}{price_fraction}".replace(',', '.'))
    return price

def send_notification(price):
    address= 'franta-cornelia@gmx.at'
    my_email = 'frantacorneliat@yahoo.com'
    password = 'hjfzfdoralgziqpd'
    subject = "I found a deal for you"
    text = f'Today this product: {product_name} only costs {price} €. \n That is below your target price. \n Be quick and get it now!! \n {PRODUCT_URL}'.encode('utf-8').strip()
    message = f"Subject:{subject}\n\n{text}"
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=address, msg=message)

if get_price() < TARGET_PRICE:
    send_notification(get_price())
