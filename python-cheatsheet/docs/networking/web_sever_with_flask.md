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

The output of the endpoint is not just the string ``Hello World`` but it is a full HTML page with the string added to
the body.
The html page is rendered by flask.

### Method 2: using the ``app.run``

If we make sure that the code is executed as a script with the ``__name__`` guard, flask can be executed as a normal
script

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
All you have to do is provide the **name** of the template and the **variables** you want to pass to the template engine
as keyword arguments.

Flask will look for templates in the **templates folder**.
So if your application is a module, this folder is next to that module, if it’s a package it’s actually inside your
package:

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
  <link rel="stylesheet" href="static/style.css"/>
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
  # create a blog endpoint on api.npoint.io
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

> When `url_for` refers to a route the argument is the  **method name associated to the route**

> When `url_for` refers to a static resource the resources is relative to the `static` folder
`url_for('static', filename='files/cheat_sheet.pdf')`

## Templating html pages

We can define a base structure for multiple pages, with common parts
on separate html files and make the children pages define the specific parts only.

### Base template

```html
<!DOCTYPE html>
<html lang="en">

<head>
  ...
  <!--    Url for static resource-->
  <link href="{{ url_for('static', filename='css/styles.css') }}" rel="stylesheet">
</head>

<body>

{% include "navbar.html" %}

{% block header %}
{% endblock %}

{% block content %}
{% endblock %}

{% include "footer.html" %}

...
<script src="{{ url_for('static', filename='js/scripts.js') }}"></script>

</body>
</html>
```

### Sub parts included

`{% include "navbar.html" %}`

file `navbar.html`

```html

<nav class="navbar navbar-expand-lg navbar-light" id="mainNav">
  <div class="container px-4 px-lg-5">

    ...

  </div>
</nav>
```

it is the same for the other `include`

``{% include "footer.html" %}``

### Customizable parts as ``{% block <name> %}``

```html
{% block header %}
{% endblock %}

{% block content %}
{% endblock %}
```

### Html files defining the blocks

A file can be built as **extension** of the `base.html` file

```html
{% extends "base.html" %}

{% block title %}
Home
{% endblock %}

{% block header %}

<header class="masthead"
<!-- Some html content for the header-->
</header>

{% endblock %}

{% block content %}

<!-- Main Content-->
<div class="container px-4 px-lg-5">
  <!-- Some html content for the content-->
</div>

{% endblock %}
```

### Process data from a form with POST actions

We can define a POST method handler in Flask which
has access to a `request` object containing the fields as form data in
the request itself

https://flask.palletsprojects.com/en/stable/quickstart/#the-request-object

form sample

```html
<!--Without the action attribute the post will happen on the same url-->
<form novalidate method="post">
  <input class="form-control" name="name" type="text" placeholder="Enter your name..." required/>
  <input class="form-control" name="email" type="text" placeholder="Enter your email.." required/>
  {% if submitted_data and error == None %}
  <div id="submitSuccessMessage">
    <div class="text-center mb-3">
      <ul>
        <li>{{ submitted_data["name"]}}</li>
        <li>{{ submitted_data["email"]}}</li>
      </ul>
    </div>
  </div>
  {% endif %}
  <!-- Submit error message-->
  <!---->
  <!-- This is what your users will see when there is-->
  <!-- an error submitting the form-->
  {% if error %}
  <div id="submitErrorMessage">
    <div class="text-center text-danger mb-3">Error: {{ error }}</div>
  </div>
  {% endif %}
  <button class="btn btn-primary text-uppercase" type="submit">Send</button>

</form>
```

```python
@app.route("/contact", methods=["GET", "POST"])
def contact_page():
  error = None
  data = {}

  if request.method == 'POST':
    data["name"] = request.form.get("name")
    data["email"] = request.form.get("email")
    if request.form.get("message") is None or request.form.get("message") == "":
      error = "Please enter a message"
    else:
      data["message"] = request.form.get("message")
  return render_template("contact.html", submitted_data=data, error=error)
```

## Using WTForms with Flask-WTF

https://wtforms.readthedocs.io/en/3.0.x/

WTForms is a flexible forms validation and rendering library for Python web development. It can work with whatever web
framework and template engine you choose. It supports data validation, CSRF protection, internationalization (I18N), and
more.

### Installation

```pip install Flask-WTF```

### Create a form

https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/

https://wtforms.readthedocs.io/en/3.0.x/fields/#basic-fields

A form can be defined as a class

```python
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

# This is used for the csrf token in the form in the html file
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


class BookForm(FlaskForm):
  title = StringField('Book title', validators=[DataRequired(), Length(1, 64)])
  author = StringField("The author", validators=[DataRequired(), Length(1, 64)])
  rating = SelectField(
    "Rate the book",
    choices=[(str(i), str(i)) for i in range(1, 10)],
    coerce=int
  )
  submit = SubmitField('Submit')


class ChangeBookRating(FlaskForm):
  rating = SelectField(
    "Rate the book",
    choices=[(str(i), str(i)) for i in range(1, 10)],
    coerce=int
  )
  submit = SubmitField('Submit')


@app.route("/add", methods=["GET", "POST"])
def add():
  form = BookForm()
  if form.validate_on_submit():
    try:
      new_book = Book(
        title=form.title.data,
        author=form.author.data,
        rating=form.rating.data
      )
      db.session.add(new_book)
      db.session.commit()  # needed to persist the data
      return redirect(url_for("home"))
    except:
      db.session.rollback()
      return redirect(url_for("home"))
  return render_template("add.html", form=form)


```

Prefill form inputs with data class instance

```python
@app.route("/change_rating/<int:book_id>", methods=["GET", "POST"])
def change_rating_page(book_id):
  book = db.session.get(Book, book_id)
  form = ChangeBookRating(obj=book)
  if request.method == "GET":
    return render_template("change_rating.html", form=form, book=book)
  else:
    db.session.query(Book).filter_by(id=book_id).update({
      Book.rating: form.rating.data
    })
    db.session.commit()
    return redirect(url_for("home"))
```

The form can be rendered in the html file

```html

<form method="POST" action="{{ url_for('login_page') }}" novalidate>
  {{ form.csrf_token }}
  <!-- For each field in the form -->
  <p>
    {{ form.
    <field_name>.label }} <br> {{ form.
      <field_name>(size=30) }}
        {% for error in form.
        <field_name>.errors %}
          <span style="color: red;">[{{ error }}]</span>
          {% endfor %}
  </p>

  {{ form.submit }}
</form>
```

#### Use custom field validators

The validator function is

```python
def validate_<


  fieldname > (self, field):
pass
```

So, if we want to add validation to the `title` field we have to create a function `validate_title`

Updated form

```python
from wtforms.validators import ValidationError


class BookForm(FlaskForm):
  title = StringField('Book title', validators=[DataRequired(), Length(1, 64)])
  author = StringField("The author", validators=[DataRequired(), Length(1, 64)])
  rating = SelectField("Rate the book", choices=range(1, 10), validators=[DataRequired()])
  submit = SubmitField('Submit')

  def validate_title(self, field):
    existing_book = db.session.query(Book).filter_by(title=field.data).first()
    if existing_book:
      raise ValidationError("This book already exists in the database.")
```

When you call:

`form.validate_on_submit()`
WTForms will:

Loop over all fields in the form

* Run built-in validators (DataRequired, Length)
* Look for a method named `validate_<fieldname>`

Then automatically call:

`validate_title(self, field)`

If a `ValidationError` is raised → form is invalid

To show the error

```python
{{form.title.label}}
{{form.title(


class ="form-control")}}

{% for error in form.title.errors %}
< div


class ="text-danger" > {{error}} < / div >


{ % endfor %}
```

#### Add support for ``bootstrap-flask``

``pip install boostrap-flask``

Add to main.py

```python
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap = Bootstrap5(app)  # initialise bootstrap-flask
```

In the `base.html`

```html

<head>
  {% block styles %}
  <!-- Load Bootstrap-Flask CSS here -->
  {{ bootstrap.load_css() }}
  <!-- Link to the styles.css here to apply styling to all the child templates.-->
  <link
          rel="stylesheet"
          href="{{ url_for('static', filename='css/styles.css') }}"
  />
  {% endblock %}
  ...
  <head>
```

#### Use the bootstrap ``render_form()``

This allows to rendere the labels, input and error tags of the form with one directive

```html
{% from 'bootstrap5/form.html' import render_form %}

{% block content %}
<div class="container">
  <div class="row">
    <div class="col-sm-12 col-md-8">
      <h1>Add a new cafe into the database</h1>

      {{ render_form(form, novalidate=True) }}

      <p class="space-above">
        <a href="{{ url_for('cafes') }}">See all cafes</a>
      </p>
    </div>
  </div>
</div>
{% endblock %}
```

## Use session management with Flask-login

https://flask-login.readthedocs.io/en/latest/

Flask-Login provides user session management for Flask.
It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of
time.

### Configuration

Install the package

```bash
pip install flask-login
```

The most important part of an application that uses Flask-Login is
the [LoginManager](https://flask-login.readthedocs.io/en/latest/#flask_login.LoginManager) class.
You should create one for your application somewhere in your code, like this:

```python
from flask_login import LoginManager

login_manager = LoginManager()
```

The login manager contains the code that lets your application and Flask-Login work together, such as how to load a user
from an ID, where to send users when they need to log in, and the like.
Once the actual application object has been created, you can configure it for login with:

```python
login_manager.init_app(app)
```

By default, Flask-Login uses sessions for authentication.

This means you must set the secret key on your application, otherwise Flask will give you an error message telling you
to do so.

See the [Flask documentation on sessions](https://flask.palletsprojects.com/en/latest/quickstart/#sessions) to see how
to set a secret key.

### Create the load user callback

```python
@login_manager.user_loader
def load_user(user_id):
  return User.get(user_id)
```

### Configure the User model class requirements

https://flask-login.readthedocs.io/en/latest/#your-user-class

```python
# Define User model with UserMixin. Thanks to UserMixin our user have 3 extra features😀: is_active,
# is_authenticated, is_anonymous
class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), unique=True, nullable=False)
  password = db.Column(db.String(100), nullable=False)
  name = db.Column(db.String(1000))

```

### Add the logged user onto the session

The `login_user(user)` function does it

```python
@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'GET':
    return render_template("register.html")
  else:
    user = User()
    user.email = request.form['email']
    user.name = request.form['name']
    user.password = generate_password_hash(password=request.form['password'], method='pbkdf2:sha256', salt_length=8)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return render_template("secrets.html", name=request.form.get('name'))
```

Or during login

```python
@app.route('/login', methods=["GET", "POST"])
def login():
  if request.method == "POST":
    email = request.form["email"]
    password = request.form["password"]
    user = db.session.execute(db.select(User).where(User.email == email)).scalar()

    if check_password_hash(user.password, password):
      login_user(user)
      return redirect(url_for('secrets', name=user.name))
    else:
      flash("Invalid email or password. Please try again.")
      return redirect(url_for('login'))
  return render_template("login.html")
```

### Logout user

The same way we can delete a user from the session with `logout_user()`


```python
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
```

### Access logged in user in template

Using the `current_user`

```html
{% if not current_user.is_authenticated %}
<li class="nav-item">
  <a class="nav-link" href="{{ url_for('login') }}">Login</a>
</li>
<li class="nav-item">
  <a class="nav-link" href="{{ url_for('register') }}">Register</a>
</li>
{% endif %}
{% if current_user.is_authenticated %}
<li class="nav-item">
  <p class="navbar-text">Hello {{ current_user.name }}</p>
</li>
<li class="nav-item">
  <a class="nav-link" href="{{ url_for('logout') }}">Log Out</a>
</li>
{% endif %}
```

### Protecting routes

https://flask-login.readthedocs.io/en/latest/#protecting-views

```python
@app.route('/secrets/<name>')
@login_required
def secrets(name):
    return render_template("secrets.html", name=name)
```

Calling this view without a user authenticates will lead to `401 Unauthorized` code returned.

## Flask Flash messages

Sometimes, you will want to give the user some feedback on an action they took. e.g. 
Was there an issue with login in? Are they typing in the wrong password or does their email not exist? It would be a good user experience if, in these situations, we told them what was wrong, instead of just constantly redirecting them back to the login page.

The easiest way to do this is through Flask Flash messages. They are messages that are sent to the template to be rendered just once. And they disappear when the page is reloaded.

https://flask.palletsprojects.com/en/2.3.x/patterns/flashing/

```python
from flask import flash
```
Use the `flash` method to add messages
```python
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets', name=user.name))
        else:
            flash("Invalid email or password. Please try again.")
            return redirect(url_for('login'))
    return render_template("login.html")
```

```html
{% with messages = get_flashed_messages() %}
{% if messages %}
{% for message in messages %}
<p>{{ message }}</p>
{% endfor %}
{% endif %}
{% endwith %}
```