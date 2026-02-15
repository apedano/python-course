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
## List of values

```python
res_list = list(programming_dictionary.values())
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