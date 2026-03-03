# 🐍 Working with JSON files

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

## Read with `json.load()`

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

