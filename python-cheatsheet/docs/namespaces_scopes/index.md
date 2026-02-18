# 🐍 Namespace and scopes

Python manages **namespaces** as dictionaries that map:

* Variable names

* Function names

* Class names

* to their corresponding objects in memory to avoid name conflicts

## Built-in, Global and Local Scope

The built-in namespace contains the names of all of Python’s built-in objects. 
This namespace is available while the Python interpreter is running. 
So, you can access the names that live in this namespace at any time in your code without explicitly importing them.

You can list the objects in the built-in namespace with the dir() function using the __builtins__ object as an argument:
```python
>>> dir(__builtins__)
[
    'ArithmeticError',
    'AssertionError',
    'AttributeError',
    'BaseException',
    ...
    'super',
    'tuple',
    'type',
    'vars',
    'zip'
]
```

You may recognize some objects here, such as built-in exceptions, built-in functions, and built-in data types. Python creates the built-in namespace when it starts and keeps it active until the interpreter terminates.


Global scope 
````python
my_var = 10

def my_function_using_local_scope():
    my_var = 1
    print("muy_var in local scope value is :") #1

def my_function_using_global_scope():
    print("muy_var in local scope value is :") #10
    
print("muy_var in global scope value is :") #10
````

```python
def my_function():
    my_function_scoped = "value"
    def my_inner_function() :
        my_inner_scoped_variable = "value2"
        print(f"{my_function_scoped}", f"{my_inner_scoped_variable}")
    my_inner_function()
        
my_function() #value value2
my_inner_function() #NameError: name 'my_inner_function' is not defined
```
## The LEGB Rule

Python resolves names using the LEGB rule:

_Local_

_Enclosing_

_Global_

_Built-in_

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)
    inner()
outer()
```
Output: `local`

## Using `glocal`

Allows modifying a global variable inside a function.

Always show details
```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count) #1
```

Without global, Python would create a local variable instead.

## `nonlocal` Keyword

Used in nested functions to modify a variable in the enclosing namespace.

Always show details

```python
def outer():
    x = 10
    
    def inner():
        nonlocal x
        x += 5
    
    inner()
    print(x)

outer() #15
```

## Inspecting Namespaces

### `globals()`

Returns the global namespace dictionary.

Always show details
```python
print(globals())
```

### `locals()`

Returns the current local namespace dictionary.

Always show details

```python
def test():
    a = 5
    print(locals())

test() # {'a': 5}
```




