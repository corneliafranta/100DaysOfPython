from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        fresult = function()
        return f'<b>{fresult}</b>'
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        fresult = function()
        return f'<em>{fresult}</em>'
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        fresult = function()
        return f'<u>{fresult}</u>'
    return wrapper_function


@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return "Hej"



if __name__ == '__main__':
    app.run(debug=True)