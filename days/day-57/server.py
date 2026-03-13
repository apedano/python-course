import datetime
import random

import requests
from flask import Flask, render_template

def load_posts():
    response = requests.get("https://api.npoint.io/74667564fb06136648b8")
    response.raise_for_status()
    return response.json()

app = Flask(__name__)
blog_posts = load_posts()

@app.route("/")
def hello_world():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", random_number=random_number, year=current_year)

@app.route("/guess/<string:name>")
def gueass(name):
    name_title = name.title()
    params = {
        "name": name_title
    }
    response = requests.get("https://api.genderize.io/", params=params)
    response.raise_for_status()
    gender = response.json()["gender"]
    response = requests.get("https://api.agify.io/", params=params)
    age = response.json()["age"]
    return render_template("guess.html", name =name, age=age, gender=gender)

@app.route("/blog_raw")
def get_blog_raw():
    #create a blog endpoint on api.npoint.io

    return blog_posts

@app.route("/blog")
def get_blog():
    #create a blog endpoint on api.npoint.io
    return render_template("blog.html", posts=blog_posts)




if __name__ == "__main__":
    app.run(debug=True, port=5001)
