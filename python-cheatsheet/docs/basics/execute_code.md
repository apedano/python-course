# 🐍 Execute Python code

### The `__name__` special attribute

In Python, every file has a built-in variable called `__name__`.

If the file is run directly:

```bash
python app.py
```

then:

``__name__ == "__main__"``

If the file is imported by another script (or module):

```python
import app
```

then:

``__name__ == "app"``

If `app.run()` is not protected, it will run every time the module is imported, which is usually not what you want.

Wrong example (what the warning complains about)

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

app.run()
```

>If another file imports this module, the server would start automatically.

Correct way

Wrap it in this guard:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
return "Hello"

if __name__ == "__main__": #the execution entry point is this file
app.run()
```

Now:
```
python app.py → server starts

import app → server does not start
```

Why frameworks require this

This pattern helps with:

testing

importing the app from other modules

running with production servers (like gunicorn)

✅ Rule of thumb:
Anything that should only run when the file is executed (not imported) goes inside:

```if __name__ == "__main__":```
