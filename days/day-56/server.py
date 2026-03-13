from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("personal-site.html")

@app.route("/personal-site")
def personal_site():
    return render_template("personal-site.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
