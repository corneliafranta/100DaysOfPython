import os

import requests
from twilio.rest import Client
from twilio.http.http_client import  TwilioHttpClient

api_key = "b74e9e41e9a292abf7d3dcc166c0a3ed"
params = {
    'lat': 61.45217,
    'lon': 5.85717,
    'exclude': "current,minutely,daily",
    'appid': api_key

}
response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=params)
response.raise_for_status()
weather_data = response.json()


def send_notification():
    account_sid = 'AC59d31d79714c9aa19d6b571e12f52590'
    auth_token = '6906b4c9d3d41d27978bbc980ed2312e'

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies ={'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella 🌧☂ ",
        from_='+17166870562',
        to='+436804026969'
    )
    print(message.status)


def will_rain_today(hourly_data):
    rainy_hours = [hour for hour in hourly_data if will_rain(hour['weather'][0]['id'])]
    return len(rainy_hours) > 0


def will_rain(weather_code):
    return weather_code < 700


if will_rain_today(weather_data['hourly']):
    send_notification()

