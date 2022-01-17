import os
from datetime import datetime

from flight_search import FlightSearch
from twilio.rest import Client


class FlightData:
    def __init__(self, flight_search: FlightSearch):
        self.flight_search = flight_search
        self.flight_info = flight_search.search_for_flight_to_locations()

    def send_notification(self, flight):
        from_dest = flight['cityFrom']
        to_dest = flight['cityTo']
        stay_durration = flight['nightsInDest']
        price = flight['price']
        # 2022-01-19T14:30:00.000Z
        from_dep = flight['route'][0]['local_departure'].split('T')[0]
        to_dep = flight['route'][1]['local_departure'].split('T')[0]
        link = flight['deep_link']

        text = f"Pack your bags!\n We found a flight for you 😀✈ \n" \
               f"{from_dest} - {to_dest} \n" \
               f"Price: {price}€ \n" \
               f"Departure: {from_dep} \n" \
               f"You'll stay {stay_durration} nights \n" \
               f"Book this flight: {link}"

        account_sid = os.environ.get('TWILIO_SID')
        auth_token = os.environ.get('TWILIO_TOK')
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=text,
            from_='+17166870562',
            to='+436602045529'
        )
        print(message.status)
