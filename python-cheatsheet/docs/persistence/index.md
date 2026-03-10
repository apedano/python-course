# 🐍 Persistence solutions

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