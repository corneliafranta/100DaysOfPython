import requests
from flask import Flask, render_template

app = Flask(__name__)


def get_data():
    response = requests.get('https://api.npoint.io/4ee1dd34061bec60fb90')
    return response.json()


blog_data = get_data()


@app.route('/')
def home():
    return render_template('index.html', posts= blog_data )


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in blog_data:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
