from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from user_manager import UserManager

data_manager = DataManager()
flight_search = FlightSearch(data_manager.destinations)
flight_data = FlightData(flight_search)
user_manager = UserManager(data_manager)


def updata_all_iafa_codes():
    for destination in data_manager.destinations:
        iafa_key = flight_search.get_iafa_code(destination['city'])
        data_manager.add_iafa_code(destination=destination, code=iafa_key)


def send_info():
    for flight in flight_data.flight_info:
        flight_data.send_notification(flight)

user_manager.create_user()