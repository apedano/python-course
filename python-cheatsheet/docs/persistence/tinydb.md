# 🐍 Persistence with TinyDB

## Intro

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

## How to persist multiple classes in the same DB

### Add a discriminator field to classes

We can add a `_type` field to the classes to be persisted

The following class has a constructor (normally `@dataclass` does not require it) accepting `**kwargs` at the end.
This way we can accept additional parameters, including `_type`

```python
@dataclass
class FlightSearchData:
    origin: str
    iata_code_origin: str
    destination: str
    iata_code_destination: str
    lowe_price: float

    def __init__(self, origin:str, iata_code_origin:str, destination:str, iata_code_destination:str, lowe_price:float, **kwargs):
        self.origin = origin
        self.iata_code_origin = iata_code_origin
        self.destination = destination
        self.iata_code_destination = iata_code_destination
        self.lowe_price = lowe_price
```

### Data store manager for multiple classes


```python
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.db = TinyDB("db.json")

    def init_database(self, initial_data:list[fd.FlightSearchData]):
        self.db.truncate()
        for item in initial_data:
            self.db.insert(self.__to_dict(item))

    def get_all_flight_search_data(self) -> list[fd.FlightSearchData]:
        Item = Query()
        # Get all users
        all_flight_search_data = self.db.search(Item._type == "FlightSearchData")
        all_data_list = []
        for data in all_flight_search_data:
            all_data_list.append(fd.FlightSearchData(**data))
        return all_data_list

    # Convert objects to dictionaries
    @staticmethod
    def __to_dict(obj):
        return {"_type": obj.__class__.__name__, **obj.__dict__}

```

The class instaces are turned into the JSON representation to be stored in the DB using the `__to_dict(ob)` method, 
which adds the discriminator `_type` JSON attribute values with the class name. 
The rest is `**obj` that is the keyword expansion of the object.

When the object is loaded, the search is done adding the type attribute

