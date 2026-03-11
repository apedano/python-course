# 🐍 Serving requests with Flask

Flask is a Web Server Gateway Interface (WSGI) web application framework.

https://flask.palletsprojects.com/en/stable/

Installation

``python3 -m pip install flask``

## Hello world


```json
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

## How to run a flask server

### Method 1: using the flask cli

From the directory containing the file with the code above 

```bash
(.venv)$ export FLASK_APP=app.py
```

Or in powershell

```powershell
$Env:FLASK_APP = "app.py"
```

And then 

``
flask run
``

```                                                                                                                                                   
* Serving Flask app 'main.py'
* Debug mode: off
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1:5000
Press CTRL+C to quit``
```
The output of the endpoint is not just the string ``Hello World`` but it is a full HTML page with the string added to the body.
The html page is rendered by flask.

### Method 2: using the ``app.run``

If we make sure that the code is executed as a script with the ``__name__`` guard, flask can be executed as a normal script

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

