import os
from user import User

import requests

HEADER = {
    "Authorization": f"Bearer {os.environ.get('SHEETY_BAER')}"
}


class DataManager:

    def __init__(self):
        self.get_destinations()

    def get_destinations(self):
        api_address = 'https://api.sheety.co/83224b22e91653733fd023174b5e2e12/flightDeals/cities'
        response = requests.get(url=api_address, headers=HEADER)
        self.destinations = []

    def add_iafa_code(self, destination, code):
        params = {
            'city': {
                'iataCode': code
            }
        }
        url = f"https://api.sheety.co/83224b22e91653733fd023174b5e2e12/flightDeals/cities/{destination['id']}"
        response = requests.put(url=url, headers=HEADER, json=params)
        print(response)

    def add_user(self, user: User):
        url = 'https://api.sheety.co/83224b22e91653733fd023174b5e2e12/flightDeals/users'
        first_name = user.first_name
        last_name = user.last_name
        email= user.email
        print(type(first_name), type(last_name), type(email))
        params = {
            user: {
                'firstName': first_name,
                'lastName': last_name,
                'email': email
            }
        }
        print('after params')
        response = requests.post(url='https://api.sheety.co/83224b22e91653733fd023174b5e2e12/flightDeals/users', params=params, headers=HEADER)
        response.raise_for_status()
