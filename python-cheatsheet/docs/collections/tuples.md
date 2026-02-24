# 🐍 Tuple

## 1. What is a Tuple?

A **tuple** is 

- **Ordered** → Items have a defined order
- **Immutable** → Cannot be changed after creation
- **Allows duplicate** values
- Can store **mixed data types**

------------------------------------------------------------------------

## 2. Creating Tuples

``` python
# Empty tuple
empty = ()

# Tuple with values
numbers = (1, 2, 3)

# Mixed data types
mixed = (1, "hello", 3.14)

# Without parentheses (tuple packing)
packed = 1, 2, 3
```

------------------------------------------------------------------------

## 3. Accessing Tuple Elements

``` python
numbers = (10, 20, 30, 40)

print(numbers[0])   # 10
print(numbers[-1])  # 40
```

### Slicing

``` python
print(numbers[1:3])  # (20, 30)
```

------------------------------------------------------------------------

## 4. Tuple Immutability

``` python
numbers = (1, 2, 3)
numbers[0] = 10  # ❌ TypeError
```

Tuples cannot be modified after creation.

------------------------------------------------------------------------

## 5. Tuple Unpacking

``` python
point = (4, 5)

x, y = point

print(x)  # 4
print(y)  # 5
```

### Extended Unpacking

``` python
numbers = (1, 2, 3, 4, 5)

a, *middle, b = numbers
print(a)       # 1
print(middle)  # [2, 3, 4]
print(b)       # 5
```

------------------------------------------------------------------------

## 6. Tuple Methods

Tuples have only two built-in methods:

``` python
numbers = (1, 2, 2, 3)

print(numbers.count(2))  # 2
print(numbers.index(3))  # 3
```

------------------------------------------------------------------------

## 7. Useful Operations

### Length

``` python
len((1, 2, 3))  # 3
```

### Membership

``` python
3 in (1, 2, 3)  # True
```

### Concatenation

``` python
(1, 2) + (3, 4)  # (1, 2, 3, 4)
```

### Repetition

``` python
(1, 2) * 3  # (1, 2, 1, 2, 1, 2)
```

------------------------------------------------------------------------

## 8. Single-Element Tuple

Important: A single-element tuple requires a comma.

``` python
not_a_tuple = (5)     # int
real_tuple = (5,)     # tuple
```

------------------------------------------------------------------------

## 9. When to Use Tuples

Use tuples when:

-   Data should not change
-   Returning multiple values from a function
-   Using as dictionary keys
-   Storing fixed records

------------------------------------------------------------------------

## 10. Returning Multiple Values

``` python
def get_user():
    return "Alice", 30

name, age = get_user()
```

------------------------------------------------------------------------

## 11. Tuple with Loop

``` python
for item in (1, 2, 3):
    print(item)
```

------------------------------------------------------------------------
