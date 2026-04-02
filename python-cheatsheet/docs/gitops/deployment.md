#  🐍 Deploy a Flask web application

## Code preparation

### Use environment variables for secrets

where we have 
```python
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
```
We create a `FLASK_KEY` variable and then 
we should make it 

```python
import os

app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
```

### Setup a WSGI server with gunicorn

WSGI stands for **Web Server Gateway Interface** and it's described here: https://www.python.org/dev/peps/pep-3333/

> Normal web servers can't run Python applications, so a special type of server was created (WSGI) to run our Flask app.  
> Essentially, a WSGI server standardises the language and protocols between our Python Flask application and the host server.

### Setup Gunicorn

This is one of the many WSGI available. https://gunicorn.org/

Check if it is part of the `requirements.txt` file

`gunicorn==21.2.0`

We need to create a `Procfile` file in the project root with the content

`web: gunicorn main:app`

This will tell our hosting provider to create a web worker that is able to receive HTTP requests. 
The `Procfile` also says to use `gunicorn` to serve your web app. 
And finally it **specifies the Flask app** object is the `main.py` file. 
That way the hosting provider knows about the entry point for the app and what our app is called.

## Deploy to RENDER

https://dashboard.render.com/

Here we can create one free project with a Postgres service and the Python web service from the repository with the code

It is important to set the env var of the database connection to the **Internal Database URL** in the Postgres service

### Set env vars from dashboards

If necessary the python version to use can be changeds by setting the env var

`PYTHON_VERSION=<python_version>`

`PYTHON_VERSION=3.11.9`

### Sample app:

https://github.com/apedano/python-deploy-test/tree/render-deploy

Branch `render-deploy`


