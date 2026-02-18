# 🐍 Error handling

## Bae exception handling

```python
try:
    value = int("abc")
except (ValueError, TypeError):
    print("Invalid conversion!")
```

## Multiple exception handling

```python
try:
    value = int("abc")
except (ValueError, TypeError):
    print("Invalid conversion!")
```

## All exceptions handling

```python
try:
    risky_operation()
except Exception as e:
    print(f"Error occurred: {e}")
```

>Avoid using bare `except`: because it catches system-exiting exceptions too.

## `else` 

The `else` block runs if no exception occurs.
```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Success:", result)
```

## `finally`

The `finally` block always executes

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution finished")
```

## Raising exceptions

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
```

## Creating custom exceptions

```python
class CustomError(Exception):
    pass

raise CustomError("Something went wrong")
```

## Common built-in exceptions

| Exception         | Description            |
| ----------------- | ---------------------- |
| ValueError        | Invalid value          |
| TypeError         | Wrong data type        |
| ZeroDivisionError | Division by zero       |
| IndexError        | Invalid list index     |
| KeyError          | Missing dictionary key |
| FileNotFoundError | File not found         |



