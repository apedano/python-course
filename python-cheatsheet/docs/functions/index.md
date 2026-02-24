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

### Default parameters

```python
def add_ingredients(self, water_amount: int = 0, coffee_amount: int = 0, milk_amount: int = 0):
    self.water_amount = water_amount
    self.coffee_amount = coffee_amount
    self.milk_amount = milk_amount
```
This makes the function callable without not all parameters

```python
add_ingredients(water_amount=2, milk_amount=19)
```

### Functions returning a value

```python
def test_return(input_value):
    return input_value + "returned"

my_value = test_return("an input")
```

### Functions returning multiple values

```python
def test_return_multiple(input_value):
    return input_value, input_value + "returned"

original_input, input_returned = test_return_multiple("an input")

print(original_input) #an input
print(input_returned) #an inputreturned
```

### Nested functions

```python
def outer_function(a,b):
    def inner_function(c, d):
        return c+d
    return inner_function(a, b)

print(outer_function(3,5)) #8
```

### Docstring
It is used to comment functions

```python
def test_return_multiple(input_value):
    """ 
        My 
        Multiline 
        Comment
        as Docstring 
    """
    return input_value, input_value + "returned"

original_input, input_returned = test_return_multiple("an input")

print(original_input) #an input
print(input_returned) #an inputreturned
```

### High order functions

Functions using other functions as parameters

```python
def apply_operation(func, value):
    return func(value)

def square(x):
    return x * x

result = apply_operation(square, 5)
print(result)  # 25
```
