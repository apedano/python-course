#  🐍 The `time` module

## The `datetime` module

https://docs.python.org/3/library/datetime.html

```python
import datetime as dt

current_date_time = dt.datetime.now()

print(current_date_time) #
print(type(current_date_time))
```

the ouptut is

``
2026-03-03 10:51:19.290108
<class 'datetime.datetime'>
``
### The datetime object

```python
y = current_date_time.year
m = current_date_time.month
d = current_date_time.day
wd = current_date_time.weekday() #zero-based number of the day in the week
```

### Create an object


```python
my_birthday_date_time = dt.datetime(1980, 7, 27)
print(my_birthday_date_time) #1980-07-27 00:00:00

my_birthday_date = dt.date(1980, 7, 27)
print(my_birthday_date) #1980-07-27
```

### Calculate time difference

```python
three_days_ago = dt.date.today() - dt.timedelta(days=3)
```

### Sleep

````python
import time

#argument is the number of seconds
time.sleep(1)
````

### Date time formatting `strftime`

```python
from datetime import datetime

now = datetime.now()

formatted = now.strftime("%Y-%m-%d %H:%M:%S")

print(formatted)
```

| Code | Meaning       | Example |
| ---- | ------------- | ------- |
| `%Y` | 4-digit year  | 2026    |
| `%y` | 2-digit year  | 26      |
| `%m` | month (01–12) | 03      |
| `%d` | day of month  | 09      |
| `%H` | hour (24h)    | 15      |
| `%I` | hour (12h)    | 03      |
| `%M` | minute        | 42      |
| `%S` | seconds       | 10      |
| `%A` | weekday full  | Monday  |
| `%a` | weekday short | Mon     |
| `%B` | month full    | March   |
| `%b` | month short   | Mar     |
| `%p` | AM/PM         | PM      |
