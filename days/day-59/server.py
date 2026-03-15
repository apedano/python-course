import datetime
import random

import requests
from flask import Flask, render_template, request

def load_posts():
    response = requests.get("https://api.npoint.io/74667564fb06136648b8")
    response.raise_for_status()
    return response.json()

app = Flask(__name__)
blog_posts = load_posts()

@app.route("/")
def homepage():
    return render_template("index.html", posts=blog_posts)


@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    error = None
    data = {}

    if request.method == 'POST':
        data["name"] = request.form.get("name")
        data["email"] = request.form.get("email")
        if request.form.get("message") is None or request.form.get("message") == "":
            error = "Please enter a message"
        else :
            data["message"] = request.form.get("message")
    return render_template("contact.html", submitted_data=data, error=error)


@app.route("/post/<int:post_id>")
def post_page(post_id):
    post_with_id = None
    for post in blog_posts:
        if post["id"] == post_id:
            post_with_id = post
            break
    if post_with_id is None:
        raise Exception("Post not found")
    return render_template("post.html", post=post_with_id)

@app.route("/about")
def about_page():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
