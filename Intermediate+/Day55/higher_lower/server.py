import random

from flask import Flask

app = Flask(__name__)
rand_number = random.randint(0,10)

@app.route('/')
def main_page():
    image_href = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
    content = f"<h1>Guess a number between 0 and 9 </h1>" \
              f"<img src={image_href} width='400'>"
    return content

@app.route('/<int:number>')
def check_input(number):
    content: str
    if number > rand_number:
        content = "<h1>Too high, try again</h1>" \
                  "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width='400'>"
    elif number < rand_number:
        content = "<h1>Too low, try again</h1>" \
                  "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width='400'>"
    else:
        content = "<h1>You found me!!!</h1>" \
                  "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width='400'>"

    return content













if __name__ == '__main__':
    app.run(debug=True)