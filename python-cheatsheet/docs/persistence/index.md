# 🐍 Persistence solutions
  
1️⃣ TinyDB (Best choice for most cases)

TinyDB is a local document database that stores everything in JSON.

✅ Very simple
✅ No server required
✅ Query support
✅ Good for small/medium apps

Install

`pip install tinydb`

Example database

```python

from tinydb import TinyDB, Query

db = TinyDB("db.json")

db.insert({
    "name": "Alice",
    "age": 30,
    "role": "developer"
})

db.insert({
    "name": "Bob",
    "age": 40,
    "role": "manager"
})
Query data
User = Query()

result = db.search(User.age > 35)

print(result)
```

Output:

`[{'name': 'Bob', 'age': 40, 'role': 'manager'}]`

Update data

```python

db.update({"age": 31}, User.name == "Alice")
```

Delete data

```python
db.remove(User.name == "Bob")
```

Resulting JSON file

`db.json`

```json

{
"users": [
{"name": "Alice", "age": 31, "role": "developer"}
]
}
```


2️⃣ sqlite3 with JSON fields

If your app grows, SQLite is better.

It supports JSON columns and is built into Python.

Example:

```python

import sqlite3
import json

conn = sqlite3.connect("db.sqlite")

data = {
    "name": "Alice",
    "skills": ["python", "sql"]
}

conn.execute(
    "INSERT INTO users(data) VALUES (?)",
    (json.dumps(data),)
)

conn.commit()
```

3️⃣ ZODB

More advanced option.

Stores Python objects directly instead of JSON.

Used in larger Python systems.

⭐ Recommendation

For your local Python scripts, use:

👉 TinyDB

It is:

* JSON based

* simple

* very Pythonic

* perfect for small apps

Example realistic structure
project/
   app.py
   db.json

Example db.json:
```json

{
"users": [],
"settings": {},
"logs": []
}
```

💡 Tip: TinyDB also works very well with things like:

* Telegram bots
* desktop apps (Tkinter)
* automation scripts
* configuration storage