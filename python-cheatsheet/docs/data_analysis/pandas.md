# 🐍 Data analysis with Pandas

[Documentation](https://pandas.pydata.org/docs/)

## Installation

```bash
python3 -m pip install pandas
```

## Read CSV

Sample data `weather_data.csv`

```python
day,temp,condition
Monday,12,Sunny
Tuesday,14,Rain
Wednesday,15,Rain
Thursday,14,Cloudy
Friday,21,Sunny
Saturday,22,Sunny
Sunday,24,Sunny
```

```python
import pandas as pd

data = pd.read_csv("weather_data.csv")

print(data)
```

Output is nicely formatted
```python
         day  temp condition
0     Monday    12     Sunny
1    Tuesday    14      Rain
2  Wednesday    15      Rain
3   Thursday    14    Cloudy
4     Friday    21     Sunny
5   Saturday    22     Sunny
6     Sunday    24     Sunny
```

```python
print(data["temp"])
```

Output

```python
0    12
1    14
2    15
3    14
4    21
5    22
6    24
Name: temp, dtype: int64
```

## DataFrame and Series: working with rows and columns


### `DataFrame`
What pandas read is a [DataFrame](https://pandas.pydata.org/docs/reference/frame.html) object

> A `DataFrame` is Two-dimensional, size-mutable, potentially heterogeneous tabular data.

```python
print(type(data)) #<class 'pandas.DataFrame'>
```

### `Series`

A `DataFrame` composes [Series](https://pandas.pydata.org/docs/reference/series.html)

> A `Series` One-dimensional ndarray with axis labels (including time series).
> Similar to the columns in the `DataFrame` table

```python
print(type(data["temp"])) #<class 'pandas.Series'>
print(type(data.temp)) #<class 'pandas.Series'>
```
#### Series functions

```python
import pandas as pd

temp_series = data["temp"] # or data.temp

temperatures_list =temp_series.to_list()
average_temp = temp_series.mean()

print(temperatures_list) #[12, 14, 15, 14, 21, 22, 24]
print(average_temp) #17.428571428571427
print(temp_series.max()) #24
```

## Extracting columns as `Series`

```python
data = pd.read_csv("weather_data.csv")

#Extract column data (excluding the head)
day_series= data["day"]
temp_series = data["temp"]
condition_series = data.condition

print(condition_series)
```

Output
``
0     Sunny
1      Rain
2      Rain
3    Cloudy
4     Sunny
5     Sunny
6     Sunny
``

## Extracting rows as `DataFrame` 

```python
# Get data in row
monday_data=data[data.day== "Monday"]

print(monday_data) #still a DataFrame
```

Output
``
Name: condition, dtype: str
      day  temp condition
0  Monday    12     Sunny
``

#### Conversion to dict

```python
import pandas as pd

data = pd.read_csv("weather_data.csv")

data_dict = data.to_dict()

print(data_dict)
```
The ouptut is a dictionary with keys equal to the column names and values the series corresponding to that column

``{'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}``


## Create `DataFrame` from dict

```python
import pandas as pd

data_dict = {"students":["Amy", "Wine", "House"], "scores":[90, 80, 70] }
df = pd.DataFrame(data_dict)
df.to_csv("data.csv")

print(df)
```

output

``
  students  scores
0      Amy      90
1     Wine      80
2    House      70
``
The `data.csv` will contain

``
,students,scores
0,Amy,90
1,Wine,80
2,House,70
``

### Loopint through `DataFrame` with

```python
import pandas as pd 

student_dict = {"students":["Amy", "Wine", "House"], "scores":[90, 80, 70] }

student_pd = pd.DataFrame(student_dict)

for (key, value) in student_pd.items():
    print(value) (0, 90) (1, 80) (2, 70)
```
The output is 

```
0      Amy
1     Wine
2    House
Name: students, dtype: str
0    90
1    80
2    70
Name: scores, dtype: int64

```

### using `iterrows`

```python
for (index, row) in student_pd.iterrows():
    print(f"Index:{index}")
    print(f"Student:{row.students}") #row is a Series
```

```python
Index:0
Row:students    Amy
scores       90
Name: 0, dtype: object
Index:1
Row:students    Wine
scores        80
Name: 1, dtype: object
Index:2
Row:students    House
scores         70
Name: 2, dtype: object
```

### Create a dict from a 