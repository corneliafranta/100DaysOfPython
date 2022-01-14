import os
from datetime import datetime

import requests

pixela_endpoint = 'https://pixe.la/v1/users'
USER_NAME = 'cornelia'
TOKEN = os.environ.get('PIXELA_TOK')

# Create an Account
user_params = {
    'token': TOKEN,
    'username': 'cornelia',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response)

# Create Graph
graph_id = 'graph1'
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_id}"

graph_config = {
    'id': graph_id,
    'name': 'Coding Graph',
    'unit': 'hours',
    'type': 'int',
    'color': 'shibafu'
}
headers = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.put(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

# Add Data

pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_id}"
today= datetime.now()
pixel_config = {
    'date': today.strftime("%Y%m%d"),
    'quantity': '6'
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response)
