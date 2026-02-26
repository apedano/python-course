# 🐍 Working with CSV files

## Sample content

`weather_data.csv`

```csv
day,temp,condition
Monday,12,Sunny
Tuesday,14,Rain
Wednesday,15,Rain
Thursday,14,Cloudy
Friday,21,Sunny
Saturday,22,Sunny
Sunday,24,Sunny
```


## Reading a CSV file with `csv`

```python
import csv

with open("weather_data.csv") as data_file:
    reader = csv.reader(data_file)
    temperatures = []
    for row in reader:
        print(row) #Each row is ['day', 'temp', 'condition']
```
Output
```python
['day', 'temp', 'condition']
['Monday', '12', 'Sunny']
['Tuesday', '14', 'Rain']
['Wednesday', '15', 'Rain']
['Thursday', '14', 'Cloudy']
['Friday', '21', 'Sunny']
['Saturday', '22', 'Sunny']
['Sunday', '24', 'Sunny']
```