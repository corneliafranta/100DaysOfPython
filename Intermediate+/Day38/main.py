import datetime
import os
import time

import requests

exercise = input("How did you exercise today? ")

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    'x-app-id': os.environ.get('NUTRITIONIX_ID'),
    'x-app-key': os.environ.get('NUTRITIONIX_KEY')
}

exercise_params = {
    'query': exercise,
    'gender': 'female',
    'weight_kg': '73',
    'height_cm': 160,
    'age': 24
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
data = response.json()['exercises']





for object in data:
    date = str(datetime.date.today())
    local_time = time.localtime()
    local_time = time.strftime('%H:%M:%S', local_time)
    exercise = object['name'].title()
    duration = round(object['duration_min'])
    calories = round(object['nf_calories'])
    sheety_endpoint = 'https://api.sheety.co/83224b22e91653733fd023174b5e2e12/myWorkout/sheet1'

    sheety_header = {
        "Authorization": f"Bearer {os.environ.get('SHEETY_TOK')}"
    }
    adding_row_params = {
        'sheet1': {
            'date': date,
            'time': local_time,
            'exercise': exercise,
            'duration': duration,
            'calories': calories

        }
    }

    response = requests.post(url=sheety_endpoint, json=adding_row_params, headers= sheety_header)

print(response)
