# Functions

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