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
    app.run(port=5000)
```

## Debug mode

```python
if __name__ == "__main__":
    app.run(debug=True, port=5001)
```

It will
* Activate the debugger
* Activate the automatic reloader (no need to restart the server in case of a change)
  * Enables the debug mode in Flask application (shows error stacktrace in case of non catched error in an endpoint)
    * for instance
    ```python
    @app.route("/error")
    def error():
        x = 1 / 0    
    ```

## Route manager

### Url with parameters

The following converters are available in Flask-Variable Rules:

* `String` - It accepts any text without a slash(the default).
* `int` - accepts only integers. ex =23 
* `float` - like int but for floating point values ex. = 23.9
* `path` - like the default but also accepts slashes.
* `any` - matches one of the items provided.
* `UUID` = accepts UUID strings.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/greet/<name>")
def greet(name):
    return f"<p>Hello, my dear {name}!</p>"

@app.route("/num/<int:number>")
def greet(number):
    return f"<p>Here is the number: {number}!</p>"

@app.route("/main/html")
def render_html():
    return f"""
        <h1 style="text-align='center'">This is a title!</p>"

    """

if __name__ == "__main__":
    app.run(port=5001)
```

## Render html pages

```python
@app.route("/main/html")
def render_html():
    return """
        <h1 style="text-align:center">This is a title!</h1>
        <p style="font-weight: bold;font-style: italic;">And this is a paragraph!</p>
        <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZG8zNno0a3ZtdGhxdG51bTVkOGc2eXBtbmxjaWoxOWZ2bnllaWR6ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/V4NSR1NG2p0KeJJyr5/giphy.gif"></img>

    """
```

## Render templates

https://flask.palletsprojects.com/en/stable/quickstart/#rendering-templates

To render a template you can use the `render_template()` method. 
All you have to do is provide the **name** of the template and the **variables** you want to pass to the template engine as keyword arguments. 


Flask will look for templates in the **templates folder**. 
So if your application is a module, this folder is next to that module, if it’s a package it’s actually inside your package:

Case 1: a module:
```
/application.py
/templates
    /index.html
```
Case 2: a package:
```
/application
    /__init__.py
    /templates
        /index.html
```

```python
@app.route("/")
def home():
    return render_template("personal-site.html")
```

## Serve static files

https://flask.palletsprojects.com/en/stable/quickstart/#static-files

Static content must be placed in a `static` folder next to the server file

```
/
├── server.py
├── templates
│   └── index.html
└── static
    ├── style.css
    └── tick.gif
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="static/style.css" />
</head>
<body>
    <h1>This is the homepage title</h1>
    <p>This is a paragraph</p>
    <img src="static/tick.gif" alt="No image">
</body>
</html>
```


## Templating with Jinja

https://jinja.palletsprojects.com/en/stable/templates/

The html is rendered as a template in Flask
So in the `index.html` we can have

```html
<p>{{ 5 * 6}}</p>
```

### Pass variables to the template

The `render_template` method takes a `**context` parameter for a unlimited number of keyword arguments (`**kwargs`) 

```python
@app.route("/")
def hello_world():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", random_number=random_number, year=current_year)
```

And in the `index.html` file

```html
    <p>This is the value of the <b>random_number</b> variable: <em>{{random_number}}</em></p>
    <footer>
        <p style="text-align: right">@Copyright {{year}}</em></p>
    </footer>
```

### Templating the html content

```python
@app.route("/blog")
def blog():
    #create a blog endpoint on api.npoint.io
    response = requests.get("https://api.npoint.io/74667564fb06136648b8")
    response.raise_for_status()
    blog_posts = response.json()
    return render_template("blog.html", posts=blog_posts)
```
#### `for`
```html
    {% for post in posts %}
        <h1>{{post.title}}</h1>
        <h2>{{post.subtitle}}</h2>
        <p>{{post.body}}</p>
    {% endfor %}
```
```
loop.index
loop.index0
loop.first
loop.last
loop.length
loop.revindex
loop.revindex0
```

```html
{% for item in items %}
  {{ loop.index }} - {{ item }}
{% endfor %}
```

#### `if`

```html
{% if user %}
  Hello {{ user.name }}
{% elif guest %}
  Hello guest
{% else %}
  Hello stranger
{% endif %}
```

### Add url to be routed to `url_for()`
The input is the name of the function in the Flask server definition

```python
@app.route("/blog")
def get_blog():
    ...
```

```html
<p>Go to <a href="{{ url_for('get_blog') }}" target="_blank">blog</a></p>
```

```python
from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
```