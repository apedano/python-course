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