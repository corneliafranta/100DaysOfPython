import datetime as dt
import random
import smtplib

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1997, month=12, day=15, hour=3)


# Challenge 1

def is_wednesday():
    today = dt.datetime.now()
    return today.weekday() == 2


def send_email(address):
    quotes = get_quotes()
    my_email = 'frantacorneliat@yahoo.com'
    password = 'hjfzfdoralgziqpd'
    if is_wednesday():
        subject = "A bit of motivation"
        text = random.choice(quotes)
        message = f"Subject:{subject}\n\n{text} \n\n I love you \n Cornelia"
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=address, msg=message)


def get_quotes():
    with open("quotes.txt", 'r') as file:
        text = file.read()
        quotes = text.split('\n')
        return quotes


send_email('svenvarennes@gmail.com')
