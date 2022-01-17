from user import User
from data_manager import DataManager

class UserManager:
    def __init__(self, data_manager: DataManager):
        self.users = []
        self.data_manager = data_manager

    def create_user(self):
        print('Welcome to Flight Club \n'
              'WE find the best flight deals and email you!')
        first_name = input('What is your first name? ')
        last_name = input('What is your last name? ')
        email = input('What is your email address? ')
        user = User(first_name, last_name, email)
        self.users.append(user)
        self.save_user(user)

    def save_user(self, user: User):
        self.data_manager.add_user(user)
        print('Account got created')

