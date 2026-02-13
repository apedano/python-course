#  🐍`while`

## 📌 What is a `while` Loop?

A `while` loop repeatedly executes a block of code **as long as a
condition is `True`**.

It is useful when: - The number of iterations is **not known in
advance** - You want to repeat something **until a condition changes**

------------------------------------------------------------------------

## 🧱 Basic Syntax

``` python
while condition:
    # code block
```

-   The `condition` is checked **before each iteration**
-   If `condition` becomes `False`, the loop stops

------------------------------------------------------------------------

## 🔁 Simple Example

``` python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### ✅ Output:

    1
    2
    3
    4
    5

------------------------------------------------------------------------

## ⚠️ Avoid Infinite Loops

``` python
while True:
    print("This runs forever!")
```

Stop manually with `Ctrl + C`.

------------------------------------------------------------------------

## 🛑 Using `break`

``` python
while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input == "exit":
        break
    print("You typed:", user_input)
```

------------------------------------------------------------------------

## ⏭ Using `continue`

``` python
number = 0

while number < 5:
    number += 1
    if number == 3:
        continue
    print(number)
```

------------------------------------------------------------------------

## 🔄 `while` with `else`

``` python
x = 1

while x < 4:
    print(x)
    x += 1
else:
    print("Loop finished successfully!")
```

------------------------------------------------------------------------

## 📝 Cheat Sheet

``` python
while condition:
    # repeat code

break       # exit loop
continue    # skip iteration
else        # runs if loop ends normally
```

------------------------------------------------------------------------

## ✅ Summary

-   Runs while condition is True
-   Update variables to avoid infinite loops
-   Use `break` to exit early
-   Use `continue` to skip iterations
