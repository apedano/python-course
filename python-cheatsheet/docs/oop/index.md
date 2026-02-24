# 🐍 Object-Oriented Programming (OOP) in Python

## 1. Introduction to OOP

Object-Oriented Programming (OOP) is a programming paradigm based on the
concept of **objects**. Objects contain: - **Attributes** (data) -
**Methods** (functions)

Python is a multi-paradigm language that fully supports OOP.

------------------------------------------------------------------------

## 2. Defining a Class

A class is a blueprint for creating objects.

``` python
class Person:
    pass
```

------------------------------------------------------------------------

## 3. The `__init__` Constructor

The constructor initializes object attributes.

``` python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 30)
print(p1.name)  # Alice
```

- `self` refers to the instance of the class.
- `__init__` runs automatically when creating a new object.

------------------------------------------------------------------------

## 4. Instance Methods

Methods are functions defined inside a class.

``` python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"

p = Person("Bob")
print(p.greet())
```

------------------------------------------------------------------------

## 5. Class Attributes vs Instance Attributes

``` python
class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

d1 = Dog("Rex")
print(d1.species)
```

- Class attributes are shared across all instances.
- Instance attributes are unique per object.

------------------------------------------------------------------------

## 6. Encapsulation - private attributes/methods

Encapsulation restricts direct access to some attributes.

``` python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__validate_amount(amount)  # Calling private method
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    # Private method
    def __validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
```

- Prefixing with `__` makes it name-mangled (pseudo-private).

------------------------------------------------------------------------

## 7. Inheritance

Inheritance allows a class to inherit behavior from another class.

``` python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

d = Dog()
print(d.speak())
```

- `Dog` inherits from `Animal`.
- Method overriding allows redefining parent methods.

------------------------------------------------------------------------

## 8. Polymorphism

Polymorphism allows different classes to use the same method name.

``` python
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

for animal in [Cat(), Dog()]:
    print(animal.speak())
```

------------------------------------------------------------------------

## 9. Abstraction (Using ABC)

Python provides abstract base classes via the `abc` module.

``` python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

------------------------------------------------------------------------

## 10. Class Methods and Static Methods

``` python
class MyClass:

    class_variable = 10

    @classmethod
    def class_method(cls):
        return cls.class_variable

    @staticmethod
    def static_method(x, y):
        return x + y
```

- `@classmethod` works with class-level data.
- `@staticmethod` does not access class or instance.

------------------------------------------------------------------------

## 11. Magic (Dunder) Methods

Special methods start and end with double underscores.

``` python
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

b = Book("Python 101")
print(b)
```

Common magic methods:

| Magic Method | When It Is Called                         | Short Explanation                                                 | Example           |
|--------------|-------------------------------------------|-------------------------------------------------------------------|-------------------|
| `__init__`   | When an object is created                 | Initializes (constructs) a new object and sets up its attributes. | `obj = MyClass()` |
| `__str__`    | When using `print()` or `str()`           | Returns a user-friendly string representation of the object.      | `print(obj)`      |
| `__repr__`   | When using `repr()` or in the interpreter | Returns an unambiguous, developer-oriented string representation. | `repr(obj)`       |
| `__len__`    | When using `len()`                        | Returns the length of an object.                                  | `len(obj)`        |
| `__eq__`     | When using `==`                           | Defines equality comparison between two objects.                  | `obj1 == obj2`    |

------------------------------------------------------------------------

## 12. Composition

Composition means using objects inside other objects.

``` python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()

car = Car()
print(car.start())
```

------------------------------------------------------------------------

## 13. Dataclasses (Modern OOP)

Python provides `dataclasses` to reduce boilerplate.

``` python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u = User("Alice", 30)
print(u)
```

------------------------------------------------------------------------

# Summary

OOP in Python includes:

- Classes and Objects
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
- Composition
- Magic Methods
- Dataclasses

OOP helps structure large programs and improves reusability and
maintainability.
