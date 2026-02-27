#  🐍 Functions

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

### `*args` for any number of positional arguments

> `*args` is a conventional name, the important is the `*` in front of the name
> The `args` is a **tuple** we can loop through

```python
def add(*args):
    for n in args:
        print(n)
```

```python
def add(*args):
    args[0]
```

```python
def add(*args):
    return sum(args)
print(add(1,2,3,4,5,6,7,8,9)) #45
```

### `*kwargs` for any number of keyworded positional arguments

> `**kwargs` is a conventional name, the important is the `**` in front of the name
> The `kwargs` is a **dictionary** we can loop through

```python
def calculate(**kwargs):
    print(kwargs)


calculate(add=1, multiply=2) #{'add': 1, 'multiply': 2}
```
In combination with positional arguments
 
```python
#maps the kwargs to the reminder of the arguments in the call
def calculate(op, **kwargs):
    print(op)
    for key, value in kwargs.items():
        print(f"{key}->{value}")

calculate("add", a=3, b=4, c=5)
```

Use with optional keywords

```python
# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        #by using kw["make"] it might create a KeyError if the key is not passed to the constructor 
        self.make = kw.get("make") 
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
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

### Lambda expressions

A lambda expression in Python is a small, anonymous (unnamed) function defined in a single line.

```python
lambda arguments: expression
```

* It can take any number of arguments
* But only one expression
* It automatically returns the result

```python
square = lambda x: x * x

print(square(5))  # 25
```
Multiple arguments
```python
add = lambda a, b: a + b

print(add(3, 7))  # 10
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

Lamba expressions can also be used for manipulating lists

```python
numbers = [1, 2, 3, 4]

squared = list(map(lambda x: x * x, numbers))

print(squared)
# [1, 4, 9, 16]
```

Or for inline conditionals

```python
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"

print(is_even(4))  # Even
```