#  🐍Functions

## Declaration

```python
def <function name>():
    print("Hello")
    # Do something else
    # Do something else ...

def <function name_returnning>() -> str:
    print("Hello")
    # Do something else
    # Do something else ...
    return "Hello"
```
Call it
```python
<function name_returning>()

value=<function name>()
```

```python
#Creating the function
def get_user_name():
    name = input("What is your name? ")
    print("Hello, " + name)
    # Inside the function

#Outside the function
print("Hello")
get_user_name() # Calling the function
```

## Functions with input parameters

```python
# Creating the function
def myFunction(greeting, name):
    print(f"{greeting} {name}")
    
# Using the function
myFunction("Hello", "Tommy") 
# Will output "Hey! Tommy"
```

### Keyword Arguments
You can use keywords when you provide the arguments when you call a function so that there is less confusion which value is assigned to which input parameter.

```python

def greet_with_name(name, greeting):
    print(f"{greeting} {name}")

greet_with_name(name="Tommy", greeting="Hello")
```

