# 🐍 Decorators

## Class-first objects and functions

First class objects (int, str, float) can be passed as functions arguments.
But also functions (`High order functions` in the function guide)

```python

def add(x, y):
    return x+y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y


def apply_operation(func, x, y):
    return func(x,y)



result = apply_operation(add, 5, 3)
print(result)  # 8
```
Also inner function can be created

```python
def outer_function():
    print("I am outer")
    def inner_function(): #this has no visibility outside
        print("I am inner")
    inner_function()

outer_function()
```

Can be used as output

```python
def outer_function():
    print("I am outer")
    def inner_function(): #this has no visibility outside
        print("I am inner")
    return inner_function

i_f = outer_function()
i_f() #I am outer
      #I am innerI am inner
```

## Python decorator function

```python
def my_decorator_function(a_function):
    def wrapper_function():
        a_function()
    return wrapper_function 
```

So we can have control when the function argument can be actually code, so that we can execute some logic around it.

An example might be

```python
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper
```

Now we define the function argument

```python
def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
decorate() #HELLO THERE
```

## Using the `@` symbol

We can apply the decorator function in a simpler way

```python
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())
```

### Stacking decorators

Once you’re comfortable using the @ syntax for a single decorator, 
you can take it a step further and stack multiple decorators on the same function. Just keep in mind: **the order matters**! 

Below we'll define another decorator that splits the sentence into a list. 
We'll then apply the uppercase_decorator and split_string decorator to a single function.

```python
import functools
def split_string(function):
    @functools.wraps(function)
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper 
```

>Note: When stacking decorators, it's a common practice to use `functools.wraps` to ensure that the metadata of the original function is preserved
> throughout the stacking process. 
> This helps maintain clarity and consistency in debugging and understanding the properties of the decorated function.

```python
@split_string
@uppercase_decorator #applied first
def say_hi():
    return 'hello there'
say_hi()
```
The output is  
```['HELLO', 'THERE']```

## Decorators accepting arguments

```python
def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Nairobi", "Accra")
```

Output

```
My arguments are: Nairobi, Accra Cities I love are Nairobi and Accra
```

> Note: It's essential to ensure that the number of arguments in the decorator (`arg1`, `arg2` in this example) matches 
> the number of arguments in the wrapped function (`cities` in this example). 
> This alignment is crucial to avoid errors and ensure proper functionality when using decorators with arguments.

### Generify with ``*args`` and `**kwargs`

To define a general purpose decorator that can be applied to any function we use `*args` and `**kwargs`. 
*args and **kwargs collect all positional and keyword arguments and stores them in the *args and **kwargs variables. 
*args and **kwargs allow us to pass as many arguments as we would like during function calls.


```python
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():    
    print("No arguments here.")

function_with_no_argument()
```
This produces

```
The positional arguments are ()
The keyword arguments are {}
No arguments here.
```
But

```python
@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c=0, d=1):
    print(a, b, c, d)

function_with_arguments(1,2,d=3)
```
Produces
```
The positional arguments are (1, 2)
The keyword arguments are {'d': 3}
1 2 0 1
```

## Passing arguments to decorator

```python
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3) :
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,decorator_arg3,
                          function_arg1, function_arg2,function_arg3))
            return func(function_arg1, function_arg2,function_arg3)

        return wrapper

    return decorator

pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_function_with_arguments(pandas, "Science", "Tools")
```
Output
```
The wrapper can access all the variables
    - from the decorator maker: Pandas Numpy Scikit-learn
    - from the function call: Pandas Science Tools
and pass them to the decorated function
This is the decorated function, and it only knows about its arguments: Pandas Science Tools
```

## Class-Based Decorators

A class-based decorator is a class with a ``__call__`` method that allows it to behave like a function.

```python
class UppercaseDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)
        return result.upper()

@UppercaseDecorator
def greet(name):
    return f"hello there {name}"  

print(greet("Ciccio"))
# Output: HELLO THERE CICCIO
```

Advantages of class-based decorators:

* **Stateful decorators**: Class-based decorators can maintain state using instance variables, unlike function-based decorators which require closures or global variables.
* **Readability**: For complex decorators,encapsulating logic in a class can make the code more organizedand easier to understand.

### Stateful decorator

```python
class UppercaseDecoratorWithState:
    def __init__(self, function):
        self.function = function
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        print(f"This is the #{self.counter} time the decorator is used")
        result = self.function(*args, **kwargs)
        return result.upper()

@UppercaseDecoratorWithState
def greet(name):
    return f"hello there {name}"  

print(greet("Ciccio"))
print(greet("Pasticcio"))
```

Output is

```
This is the #1 time the decorator is used
HELLO THERE CICCIO
This is the #2 time the decorator is used
HELLO THERE PASTICCIO
```