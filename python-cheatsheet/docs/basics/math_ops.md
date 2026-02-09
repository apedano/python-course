# Mathematical operations

## Operators

| Operator | Name                   | Example    | Result | Extra notes |
|---------:|------------------------|------------|--------|-------------|
| `+`      | Addition               | `3 + 2`    | `5`    | Works with numbers and sequences |
| `-`      | Subtraction            | `5 - 3`    | `2`    | Unary minus supported (`-x`) |
| `*`      | Multiplication         | `4 * 3`    | `12`   | Repeats sequences (`"ha" * 3`) |
| `/`      | Division               | `7 / 2`    | `3.5`  | Always returns `float` |
| `//`     | Floor division         | `7 // 2`   | `3`    | Rounds down toward −∞ (`-7 // 2 == -4`) |
| `%`      | Modulus                | `7 % 2`    | `1`    | Result has the sign of the divisor (`-7 % 2 == 1`) |
| `**`     | Exponentiation (power) | `2 ** 3`   | `8`    | Right-associative (`2 ** 3 ** 2 == 512`) |

## Ops priority **PEMDAS**

Parentheses
Exponents
Multiplication/Division
Addition/Subtraction

```python
print(3 * 3 + 3 / 3 - 3) # 7.0
```

## Math functions

### Flooring a Number
You can floor a number or remove all decimal places using the int() function which converts a floating point number (with decimal places) into an integer (whole number).

```python
int(3.738492) # Becomes 3
```

### Rounding a Number
However, if you want to round a decimal number to the nearest whole number using the traditional mathematical way, where anything over .5 rounds up and anything below rounds down. Then you can use the python round() function.

```python
round(3.738492) # Becomes 4

round(3.14159) # Becomes 3

round(3.14159, 2) # Becomes 3.14
```
### Formatting floats

```python
format(math.pi, '.12g')  # give 12 significant digits
'3.14159265359'

format(math.pi, '.2f')   # give 2 digits after the point
'3.14'

repr(math.pi)
'3.141592653589793'
```

### Assignment Operators
Assignment operators such as the addition assignment operator += will add the number on the right to the original value of the variable on the left and assign the new value to the variable.

```python
+=

-=

*=

/=
```
