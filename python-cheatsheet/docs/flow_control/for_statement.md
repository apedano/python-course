# `for` Loop

## 1. Basic Syntax

``` python
for variable in iterable:
    # code block
```

-   **variable** → Temporary name for each item
-   **iterable** → A sequence (list, tuple, string, range, etc.)
-   The loop runs once for each item in the iterable

------------------------------------------------------------------------

## 2. Looping Over a List

``` python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

Output:

    apple
    banana
    cherry

------------------------------------------------------------------------

## 3. Using `range()`

### a) Basic range

``` python
for i in range(5):
    print(i)
```

Output:

    0
    1
    2
    3
    4

### b) Start and stop

` a <= range(a, b) < b`

``` python
for i in range(2, 6):
    print(i)
```

### c) Start, stop, step

``` python
for i in range(0, 10, 2):
    print(i)
```

------------------------------------------------------------------------

## 4. Looping Over a String

``` python
for letter in "Python":
    print(letter)
```

------------------------------------------------------------------------

## 5. Looping Over a Dictionary

``` python
person = {"name": "Alice", "age": 30}

for key in person:
    print(key, person[key])
```

Better way:

``` python
for key, value in person.items():
    print(key, value)
```

------------------------------------------------------------------------

## 6. Using `enumerate()`

``` python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

------------------------------------------------------------------------

## 7. Using `break`

Stops the loop completely.

``` python
for i in range(10):
    if i == 5:
        break
    print(i)
```

------------------------------------------------------------------------

## 8. Using `continue`

Skips the current iteration.

``` python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

------------------------------------------------------------------------

## 9. `else` with `for`

Runs only if the loop finishes normally (no break).

``` python
for i in range(3):
    print(i)
else:
    print("Loop completed!")
```

------------------------------------------------------------------------

## 10. Nested Loops

``` python
for i in range(3):
    for j in range(2):
        print(i, j)
```

------------------------------------------------------------------------

## 11. List Comprehension (Compact Loop)

``` python
squares = [x * x for x in range(5)]
print(squares)
```

------------------------------------------------------------------------

## 12. Common Mistakes

❌ Modifying a list while iterating over it\
❌ Forgetting indentation\
❌ Off-by-one errors with range()

------------------------------------------------------------------------

## 13. Best Practices

✔ Use meaningful variable names\
✔ Prefer `enumerate()` when you need the index\
✔ Use list comprehensions for simple transformations\
✔ Keep loops small and readable

------------------------------------------------------------------------

## Quick Reference

  Pattern        Example
  -------------- --------------------------------------
  Basic loop     `for x in items:`
  With index     `for i, x in enumerate(items):`
  Numeric loop   `for i in range(start, stop, step):`
  Stop early     `break`
  Skip item      `continue`

------------------------------------------------------------------------

Happy coding! 🐍