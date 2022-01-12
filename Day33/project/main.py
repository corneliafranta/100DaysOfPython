import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude


def get_iss_posistion():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (iss_latitude, iss_longitude)


# Your position is within +5 or -5 degrees of the ISS position.
def is_close(lat, long):
    print(lat, long)
    print(MY_LAT, MY_LONG)
    return is_same_lat(lat) and is_same_long(long)


def is_same_lat(lat):
    return not lat > MY_LAT + 5 and not lat < MY_LAT - 5


def is_same_long(lng):
    return not lng > MY_LONG + 5 and not lng < MY_LONG - 5


def get_sunrise_sunset():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(':')[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(':')[0])
    return (sunrise, sunset)


def is_dark_outside():
    sunrise_sunset = get_sunrise_sunset()
    sunrise = sunrise_sunset[0]
    sunset = sunrise_sunset[1]
    now = datetime.now().hour
    return now > sunset or now < sunrise


def send_notification_email(email):
    my_email = 'corneliaDeGossonDeVarennes@gmail.com'
    password = '1234Test'
    subject = "LOOK UP"
    text = "The International Space station is right above you :) \n If you are lucky you might be able to see it"
    message = f"Subject:{subject}\n\n{text}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=message)





while True:
    time.sleep(60)
    iss_possition = get_iss_posistion()
    if is_dark_outside() and is_close(iss_possition[0], iss_possition[1]):
        send_notification_email('franta-cornelia@gmx.at')
