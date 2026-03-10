# 🐍 Working with JSON files

## From str to JSON

```python
import json

my_str = "{\"person\": {\"name\": \"Alessandro\", \"surname\": \"Pedano\", \"birth\": {\"city\": \"Palermo\", \"date\": \"1980-07-27\"}}}"

person_dict = json.loads(my_str) #this is a dictionary

print(person_dict["person"]["name"])
```


## Parsing Json files with `json.load()`
With the build-in module `json` we can map json content to Python `dict` two ways 

Suppose we have a file with the following content

`password_store.json`

```json
{
    "website": {
        "email": "...",
        "password": "plain_text_password"
    },
    "FB": {
        "email": "my_email@domain.com",
        "password": "9ZHI9S-C3CWGI2&508D3"
    }
}
```

```python
import json
with open("password_store.json", "r") as f:
    data = json.load(f)
```

`data` is a dict we can read

```python
data["website"]["password"] #plain_text_password
```

If the file does not contain JSON formatted data or does not exist, it will generate a 
`JSONDecodeError`

In order to solve it we can 

```python
try:
    with open(file_path, "r") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data = {}
```

## Write with `json.dump()`

```python
with open("password_store.json", "w") as f:
    json.dump(data, f, indent=4)
```

## Update with `json.update()`

```python
new_data_dict = {
    input_ws.get(): {
        "email": input_user.get(),
        "password": input_psw.get()
    }
}
try:
    with open("password_store.json", "r") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error opening password store: {e}")
    print("Creating empty store")
    data = {}

data.update(new_data_dict)
with open("password_store.json", "w") as f:
    json.dump(data, f, indent=4)
```
## JSONPATH search

In Python you typically use `jsonpath-ng`, which is one of the most complete libraries.

1️⃣ Install JSONPath library

`pip install jsonpath-ng`

2️⃣ Basic Example

```python

from jsonpath_ng import parse

data = {
    "store": {
        "book": [
            {"title": "Python 101", "price": 10},
            {"title": "Advanced Python", "price": 20}
        ]
    }
}

jsonpath_expr = parse('store.book[*].title')

matches = [match.value for match in jsonpath_expr.find(data)]

print(matches)
```

Output
```
['Python 101', 'Advanced Python']
```

### JSONPATH Syntax overview

| Expression    | Meaning           |
| ------------- | ----------------- |
| `$`           | root object       |
| `.`           | child operator    |
| `*`           | wildcard          |
| `[n]`         | array index       |
| `[start:end]` | array slice       |
| `..`          | recursive descent |
| `[?()]`       | filter            |

#### Root object access

```python
{
  "name": "Alice",
  "age": 30
}
```

```python
parse("$.name") # Alice
```

### Arrays

```python
{
 "numbers": [10,20,30]
}
```

```python
parse("$.numbers[1]") #20
```

#### Wildcard selection

```python
parse("$.store.book[*].title") #Returns all book titles.

```

#### Recursive search

```python
parse("$..price")
```

Returns all prices anywhere in the JSON tree.

Example result

`[10, 20]`


#### Filter example

JSON
```json
{
 "books": [
   {"title":"Python","price":10},
   {"title":"Java","price":30}
 ]
}

```

Query

```python
parse("$.books[?(@.price < 20)].title")
```


Result

`['Python']`

> Note: filtering support may require `jsonpath_ng.ext`.

#### Update JSON values

```python

from jsonpath_ng.ext import parse

data = {"user":{"name":"Alice"}}

expr = parse("$.user.name")

for match in expr.find(data):
    match.full_path.update(data, "Bob")

print(data)
```

Result

`{'user': {'name': 'Bob'}}`


#### Extract structured results

```python
expr = parse("$.store.book[*]")

for match in expr.find(data):
    print(match.value)
```

#### Working with complex JSON

Example JSON:
```json

{
"users":[
  {"name":"Alice","skills":["python","sql"]},
  {"name":"Bob","skills":["java"]}
  ]
}
```

Query all skills:

```python
parse("$.users[*].skills[*]")
```

Result

``['python','sql','java']``
