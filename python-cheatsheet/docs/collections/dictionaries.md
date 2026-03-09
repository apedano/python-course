# 🐍 Dictionaries

Collections of `(key, value)` elements

## Create

```python
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}#{key:value}

programming_dictionary = {
    123: "Value for 123", 
    456: "Value for 456",
}#{key:value}


empty_dictionary={}

```
## Indexing

```python
programming_dictionary["Function"]
```
## List of values `values()`

```python
res_list = list(programming_dictionary.values())
```

## List of keys `keys()`

```python
key_list = list(programming_dictionary.keys())
```

## List of items `items()`

```python
person = {
    "name": "Alice",
    "age": 30,
    "city": "Amsterdam"
}


print(person.items()) #dict_items([('name', 'Alice'), ('age', 30), ('city', 'Amsterdam')])
#Each element is a tuple ('name', 'Alice')

for key, value in person.items():
    print(key, "->", value)

```

## Keys existence value

```python
if key in my_dict:
    print("Key exists")

```

## Looping

```python
for key in programming_dictionary:
    print(f"For the key {key} the value is: {programming_dictionary[key]}")
```

```python
for key, value in programming_dictionary.items():
    print(f"{key}: {value}")
```

```python
for dict_item in programming_dictionary.items():
    print(f"The key is {dict_item[0]}")
    print(f"The value is {dict_item[1]}")
```
## Dict comprehension

### From list

Create a new dictionary out of an existing list

```python
new_dict = {new_key:new_value for item in list if condition}
```

```python
names = [
    "Liam",
    "Olivia",
    "Noah",
    "Emma",
    "Ava",
    "Elijah",
    "Sophia",
    "Mateo",
    "Isabella",
    "Lucas"
]

dict = {name:len(name) for name in names} # {'Ava': 3, 'Elijah': 6, 'Emma': 4, ...}
```

### From dict

Create a new dictionary out of an existing one

```python
new_dict = {new_key:new_value for (key, value) in dict.items() if condition} 
```

```python
import random

students_scores_dict = {name:random.randint(1,100) for name in names}
#{'Ava': 3, 'Elijah': 38, 'Emma': 15, 'Isabella': 1, 'Liam': 25, 'Lucas': 23, 'Mateo': 58, 'Noah': 87, 'Olivia': 13, 'Sophia': 49}

students_pass_exam = {name:"passed" for (name,score) in students_scores_dict.items() if score>50}
#{'Mateo': 'passed', 'Noah': 'passed'}
```


## Nesting dictionaries

```python
#list nested in dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1]) #Lille
```

```python
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])#Stuttgart
```

### Expansion `**`

`**data` expands the dictionary into keyword arguments.

```python

class User:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role


data = {
    "name": "Alice",
    "age": 30,
    "role": "Developer"
}

user = User(**data)

print(user.name)
print(user.role)
```

