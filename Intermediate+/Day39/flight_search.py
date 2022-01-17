import os

import requests

HEADERS = {
    'apikey': os.environ.get('KIWI_KEY')
}


class FlightSearch:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_iafa_code(self, name):
        url = 'https://tequila-api.kiwi.com/locations/query'
        params = {
            'term': name
        }
        response = requests.get(url=url, headers=HEADERS, params=params)
        return response.json()['locations'][0]['code']

    def get_flight(self, from_dest, to_dest, date_from, date_to, price_to):
        url = "https://tequila-api.kiwi.com/v2/search"
        params = {
            'fly_from': from_dest,
            'fly_to': to_dest,
            'date_from': date_from,
            'date_to': date_to,
            'price_to': price_to,
            'limit': 1,
            'max_stopovers': 0,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 30
        }
        response = requests.get(url=url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()['data'][0]

    def search_for_flight_to_locations(self):
        flights = []
        for destination in self.destinations:
            flight = self.get_flight('VIE', destination['iataCode'], "18/01/2022", "18/07/2022",
                                     destination['lowestPrice'])
            flights.append(flight)
            return flights
