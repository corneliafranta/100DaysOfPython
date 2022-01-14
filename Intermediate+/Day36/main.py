import os
import datetime as dt
import html
import requests
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
DIRECTION_CHAR = {'up': '🔺', 'down': '🔻'}


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


def get_stock_prices():
    today = dt.datetime.utcnow().date()
    yesterday = str(today - dt.timedelta(days=1))
    befor_yesterday = str(today - dt.timedelta(days=2))
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': 'TSLA',
        'apikey': os.environ.get('ALPHA_VAN')
    }
    response = requests.get('https://www.alphavantage.co/query', params=params)
    stock_data = response.json()['Time Series (Daily)']
    closing_price_yd = float(stock_data[yesterday]['4. close'])
    closing_price_byd = float(stock_data[befor_yesterday]['4. close'])
    return (closing_price_byd, closing_price_yd)


def compare_values(price_byd, price_yd):
    difference = price_byd - price_yd
    rising = difference > 0
    percentage = abs(difference) / price_byd * 100
    return percentage >= 3, rising, percentage


def get_news():
    params = {
        'q': COMPANY_NAME,
        'apiKey': os.environ.get('NEWS_API')
    }
    response = requests.get('https://newsapi.org/v2/everything', params=params)
    return response.json()['articles'][:3]


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def send_notification(direction, percentage, news):
    text = f"TSLA: {DIRECTION_CHAR[direction]}{percentage}%\n Headline: {news['title']} \n Brief: {news['description']} "
    account_sid = os.environ.get('TWILIO_SID')
    auth_token = os.environ.get('TWILIO_TOK')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=text,
        from_='+17166870562',
        to='+436804026969'
    )
    print(message.status)


stock_prices = get_stock_prices()
result = compare_values(stock_prices[0], stock_prices[1])
direction = ""
if result[1]:
    direction = 'up'
else:
    direction = 'down'
if result[0]:
    news = get_news()
    for article in news:
        send_notification(direction, result[2], article )

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
