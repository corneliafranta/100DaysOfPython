from datetime import date

from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    return render_template('index.html',num=random_number, year=date.today().year, name='Cornelia Franta')


if __name__ == '__main__':
    app.run(debug=True)