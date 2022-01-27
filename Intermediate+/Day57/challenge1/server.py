import requests
from flask import Flask, render_template


app = Flask(__name__)

def get_age(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    return response.json()['age']

def get_gender(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    return response.json()['gender']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<name>')
def return_gender_age(name):
    age = get_age(name)
    gender = get_gender(name)
    return render_template('guess.html', name=name, age=age, gender=gender)



if __name__ == '__main__':
    app.run(debug=True)

