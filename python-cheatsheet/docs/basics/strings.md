#  🐍Strings

## Special chars

```python
print("Hello world!\nAll the world")
```

## Concatenation

```python
print("Hello" + " " + "World")
```

## Functions

### Length `len(x)` 
```python
a="This is a string"
print(len(a))
```

## Formatting
Floats 
```python
print(f"Pi rounded: {pi:.2f}")   # 3.14
```
Or (older)
```python
print("My name is {} and I am {} years old".format(name, age))
```
With named placeholders
```python
print("My name is {n} and I am {a}".format(n=name, a=age))
```

```python
print("Pi rounded: {:.2f}".format(pi))
```

Float formatting

```python
pi = 3.1415926535
print("Pi rounded: %.2f" % pi)
```

### Common format specifiers (work with f-strings and `.format()`)

| Specifier | Meaning              |
| --------- | -------------------- |
| `.2f`     | 2 decimal places     |
| `>10`     | right align width 10 |
| `<10`     | left align           |
| `^10`     | center               |
| `,`       | thousand separator   |
| `%`       | percentage           |

```python
value = 12345.678
print(f"{value:,.2f}")   # 12,345.68
```

### Change separators

#### Format with locale

The default thousands separator is `,` and `.` for decimals.
We can change it with the locale
```python
import locale

locale.setlocale(locale.LC_ALL, "nl_NL.UTF-8")  # Dutch locale

value = 12345.678
formatted = locale.format_string("%.2f", value, grouping=True)

print(formatted)  # 12.345,68
```

>Notes:
> * Locale must be installed on your system (can fail on Windows or containers)
> * Not thread-safe in some environments
> * Affects global formatting

#### Define formatter

```python
def format_eu(n):
    s = f"{n:,.2f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")

print(format_eu(12345.678))  # 12.345,68
```
