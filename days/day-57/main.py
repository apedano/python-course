import requests
from flask import Flask, render_template

def load_posts():
    response = requests.get("https://api.npoint.io/74667564fb06136648b8")
    response.raise_for_status()
    return response.json()

app = Flask(__name__)

blog_posts = load_posts()


@app.route('/')
def home():
    return render_template("index.html", posts=blog_posts)

@app.route('/post/<int:post_id>')
def get_post(post_id):
    post_with_id = None
    for post in blog_posts:
        if post["id"] == post_id:
            post_with_id = post
            break
    if post_with_id is None:
        raise Exception("Post not found")
    return render_template("post.html", post=post_with_id)





if __name__ == "__main__":
    app.run(debug=True)
