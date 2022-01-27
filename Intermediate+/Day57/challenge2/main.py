import requests
from flask import Flask, render_template
from post import Post


app = Flask(__name__)

def get_posts():
    blog_url= 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = [Post(post['id'], post['title'], post['subtitle'], post['body']) for post in response.json()]
    return all_posts



posts = get_posts()

def find_post(id):
    for post in posts:
        if post.id == id:
            return post

@app.route('/')
def home():
    posts = get_posts()
    print(posts)
    return render_template("index.html", posts=posts)

@app.route('/posts/<int:id>')
def get_post(id):
    post = find_post(id)
    return render_template('post.html', post= post)

if __name__ == "__main__":
    app.run(debug=True)
