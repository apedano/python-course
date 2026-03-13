from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/greet/<name>")
def greet(name):
    return f"<p>Hello, my dear {name}!</p>"

@app.route("/num/<int:number>")
def greet_number(number):
    return f"<p>Here is the number: {number}!</p>"

@app.route("/main/html")
def render_html():
    return """
        <h1 style="text-align:center">This is a title!</h1>
        <p style="font-weight: bold;font-style: italic;">And this is a paragraph!</p>
        <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZG8zNno0a3ZtdGhxdG51bTVkOGc2eXBtbmxjaWoxOWZ2bnllaWR6ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/V4NSR1NG2p0KeJJyr5/giphy.gif"></img>

    """

@app.route("/error")
def error():
    x = 1 / 0

if __name__ == "__main__":
    app.run(debug=True, port=5001)
