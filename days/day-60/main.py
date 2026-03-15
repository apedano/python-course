from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap5

from login.login_form import LoginForm
import requests

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

app.secret_key = "some secret string"
bootstrap = Bootstrap5(app) # initialise bootstrap-flask

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/success")
def success_page():
    return render_template("success.html")

@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # Format: <form_object>.<form_field>.data
            print(form.email.data)
            return redirect('/success')
        else:
            return redirect('/success')
    return render_template('login.html', form=form)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
