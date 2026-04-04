# 🐍 Data analysis with Pandas

[Documentation](https://pandas.pydata.org/docs/)

## Installation

```bash
python3 -m pip install pandas
```
## Formating data

```python
pd.options.display.float_format = '{:,.2f}'.format 
```

## Read CSV

Sample data `weather_data.csv`

```python
day, temp, condition
Monday, 12, Sunny
Tuesday, 14, Rain
Wednesday, 15, Rain
Thursday, 14, Cloudy
Friday, 21, Sunny
Saturday, 22, Sunny
Sunday, 24, Sunny
```

```python
import pandas as pd

data = pd.read_csv("weather_data.csv")

print(data)
```

Output is nicely formatted

```python
         day
temp
condition
0
Monday
12
Sunny
1
Tuesday
14
Rain
2
Wednesday
15
Rain
3
Thursday
14
Cloudy
4
Friday
21
Sunny
5
Saturday
22
Sunny
6
Sunday
24
Sunny
```

```python
print(data["temp"])
```

Output

```python
0
12
1
14
2
15
3
14
4
21
5
22
6
24
Name: temp, dtype: int64
```

## DataFrame and Series: working with rows and columns

### `DataFrame`

What pandas read is a [DataFrame](https://pandas.pydata.org/docs/reference/frame.html) object

> A `DataFrame` is Two-dimensional, size-mutable, potentially heterogeneous tabular data.

```python
print(type(data))  # <class 'pandas.DataFrame'>
```

#### DataFrame functions

| Method / Attribute    | Description                            | Example                                        |
|-----------------------|----------------------------------------|------------------------------------------------|
| pd.read_csv()         | Load CSV file into a DataFrame         | df = pd.read_csv("file.csv")                   |
| df.head(n)            | First n rows (default 5)               | df.head()                                      |
| df.tail(n)            | Last n rows                            | df.tail(10)                                    |
| df.shape              | Number of rows and columns             | df.shape                                       |
| df.columns            | Column names                           | df.columns                                     |
| df.dtypes             | Data types of columns                  | df.dtypes                                      |
| df.info()             | Summary of DataFrame (types, nulls)    | df.info()                                      |
| df.describe()         | Statistical summary of numeric columns | df.describe()                                  |
| df["col"]             | Select a single column                 | df["age"]                                      |
| df[["col1","col2"]]   | Select multiple columns                | df[["age","name"]]                             |
| df.loc[]              | Label-based row/column selection       | df.loc[0:5, ["age"]]                           |
| df.iloc[]             | Position-based row/column selection    | df.iloc[0:5, 0:2]                              |
| df.at[]               | Access single value by label           | df.at[0, "age"]                                |
| df.iat[]              | Access single value by position        | df.iat[0, 1]                                   |
| df.query()            | Filter rows using expression           | df.query("age > 30")                           |
| df[df["col"] > value] | Boolean filtering                      | df[df["age"] > 30]                             |
| df.value_counts()     | Count unique values in a column        | df["city"].value_counts()                      |
| df.unique()           | Get unique values                      | df["city"].unique()                            |
| df.nunique()          | Count unique values                    | df["city"].nunique()                           |
| df.isnull()           | Detect missing values                  | df.isnull()                                    |
| df.isna()             | Detect non numeric values              | df.isna()                                      |
| df.dropna()           | New df with dropped non numeric values | clean_df = df.isna()                           |
| df.notnull()          | Detect non-missing values              | df.notnull()                                   |
| df.sample(n)          | Random sample of rows                  | df.sample(5)                                   |
| df.sort_values()      | Sort by column                         | clean_df.sort_values('Spread', ascending=True) |
| df.groupby()          | Group data for aggregation             | df.groupby("city").mean()                      |

### `Series`

A `DataFrame` composes [Series](https://pandas.pydata.org/docs/reference/series.html)

> A `Series` One-dimensional ndarray with axis labels (including time series).
> Similar to the columns in the `DataFrame` table

```python
print(type(data["temp"]))  # <class 'pandas.Series'>
print(type(data.temp))  # <class 'pandas.Series'>
```

## Extracting columns as `Series`

```python
data = pd.read_csv("weather_data.csv")

# Extract column data (excluding the head)
day_series = data["day"]
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

#### Series functions

```python
import pandas as pd

temp_series = data["temp"]  # or data.temp

temperatures_list = temp_series.to_list()
average_temp = temp_series.mean()

print(temperatures_list)  # [12, 14, 15, 14, 21, 22, 24]
print(average_temp)  # 17.428571428571427
print(temp_series.max())  # 24
```

| Method / Attribute       | Description                       | Example                |
|--------------------------|-----------------------------------|------------------------|
| df["col"]                | Select column as Series           | s = df["age"]          |
| s.head(n)                | First n values                    | s.head()               |
| s.tail(n)                | Last n values                     | s.tail(10)             |
| s.shape                  | Length of the Series              | s.shape                |
| s.index                  | Index labels                      | s.index                |
| s.values                 | Underlying array                  | s.values               |
| s.dtype                  | Data type                         | s.dtype                |
| s.describe()             | Summary statistics                | s.describe()           |
| s.mean()                 | Mean value                        | s.mean()               |
| s.median()               | Median value                      | s.median()             |
| s.min() / s.max()        | Minimum / Maximum                 | s.min(), s.max()       |
| s.idxmin() / s.idxmax()  | Index of min / max value          | s.idxmax()             |
| s.sum()                  | Sum of values                     | s.sum()                |
| s.std()                  | Standard deviation                | s.std()                |
| s.count()                | Count non-null values             | s.count()              |
| s.unique()               | Unique values                     | s.unique()             |
| s.nunique()              | Number of unique values           | s.nunique()            |
| s.value_counts()         | Frequency of unique values        | s.value_counts()       |
| s.isnull()               | Detect missing values             | s.isnull()             |
| s.notnull()              | Detect non-missing values         | s.notnull()            |
| s.fillna(value)          | Replace missing values            | s.fillna(0)            |
| s.dropna()               | Remove missing values             | s.dropna()             |
| s.astype(type)           | Convert data type                 | s.astype(int)          |
| s.sort_values()          | Sort values                       | s.sort_values()        |
| s.sort_index()           | Sort by index                     | s.sort_index()         |
| s.apply(func)            | Apply function element-wise       | s.apply(lambda x: x*2) |
| s.map(func/dict)         | Map values using function or dict | s.map({"A":1,"B":2})   |
| s.replace()              | Replace specific values           | s.replace("A","X")     |
| s.between(a, b)          | Filter values within range        | s[s.between(10, 20)]   |
| s.clip(lower, upper)     | Limit values to bounds            | s.clip(0, 100)         |
| s.iloc[]                 | Position-based access             | s.iloc[0]              |
| s.loc[]                  | Label-based access                | s.loc[s.idmax()]       |
| s.cumsum()               | Cumulative sum                    | s.cumsum()             |
| s.rolling(window).mean() | Rolling average                   | s.rolling(3).mean()    |

#### Series manipulation functions

| Method / Attribute                          | Description         | Example                                    |
|---------------------------------------------|---------------------|--------------------------------------------|
| df['col1'].subtract(df['col2'])             | Subtract (or `-`)   | diff_col = df['col1'].subtract(df['col2']) |
| clean_df.insert(<#_col>, <label>, <series>) | Insert series in DF | df.insert(1, 'Spread', diff_col)           |

#### Series String Methods (`s.str`)

| Method                   | Description                    | Example                     |
|--------------------------|--------------------------------|-----------------------------|
| s.str.lower()            | Convert to lowercase           | s.str.lower()               |
| s.str.upper()            | Convert to uppercase           | s.str.upper()               |
| s.str.title()            | Title case                     | s.str.title()               |
| s.str.strip()            | Remove leading/trailing spaces | s.str.strip()               |
| s.str.lstrip()           | Remove leading spaces          | s.str.lstrip()              |
| s.str.rstrip()           | Remove trailing spaces         | s.str.rstrip()              |
| s.str.len()              | Length of each string          | s.str.len()                 |
| s.str.contains(pat)      | Check if pattern exists        | s.str.contains("abc")       |
| s.str.startswith(pat)    | Check prefix                   | s.str.startswith("A")       |
| s.str.endswith(pat)      | Check suffix                   | s.str.endswith("Z")         |
| s.str.replace(a, b)      | Replace substring              | s.str.replace("old","new")  |
| s.str.split(sep)         | Split strings into lists       | s.str.split(",")            |
| s.str.get(i)             | Get element from split/list    | s.str.split(",").str.get(0) |
| s.str.join(sep)          | Join list elements into string | s.str.join("-")             |
| s.str.extract(regex)     | Extract regex group            | s.str.extract(r"(\d+)")     |
| s.str.findall(regex)     | Find all regex matches         | s.str.findall(r"\d+")       |
| s.str.match(regex)       | Match regex from start         | s.str.match(r"^A")          |
| s.str.pad(width)         | Pad strings to width           | s.str.pad(10)               |
| s.str.slice(start, stop) | Slice substrings               | s.str.slice(0, 3)           |
| s.str.cat(sep)           | Concatenate strings            | s.str.cat(sep=",")          |
| s.str.isnumeric()        | Check if numeric string        | s.str.isnumeric()           |
| s.str.isalpha()          | Check if alphabetic            | s.str.isalpha()             |

#### Series 📅 Datetime Methods (`s.dt`)

| Method               | Description                 | Example                             |
|----------------------|-----------------------------|-------------------------------------|
| pd.to_datetime(s)    | Convert Series to datetime  | s = pd.to_datetime(s)               |
| s.dt.date            | Extract date                | s.dt.date                           |
| s.dt.time            | Extract time                | s.dt.time                           |
| s.dt.year            | Extract year                | s.dt.year                           |
| s.dt.month           | Extract month               | s.dt.month                          |
| s.dt.day             | Extract day                 | s.dt.day                            |
| s.dt.hour            | Extract hour                | s.dt.hour                           |
| s.dt.minute          | Extract minute              | s.dt.minute                         |
| s.dt.second          | Extract second              | s.dt.second                         |
| s.dt.dayofweek       | Day of week (0=Mon)         | s.dt.dayofweek                      |
| s.dt.day_name()      | Name of day                 | s.dt.day_name()                     |
| s.dt.month_name()    | Name of month               | s.dt.month_name()                   |
| s.dt.quarter         | Quarter of year             | s.dt.quarter                        |
| s.dt.is_month_start  | Check if first day of month | s.dt.is_month_start                 |
| s.dt.is_month_end    | Check if last day of month  | s.dt.is_month_end                   |
| s.dt.tz_localize(tz) | Set timezone                | s.dt.tz_localize("UTC")             |
| s.dt.tz_convert(tz)  | Convert timezone            | s.dt.tz_convert("Europe/Amsterdam") |
| s.dt.strftime(fmt)   | Format datetime to string   | s.dt.strftime("%Y-%m-%d")           |
| s.dt.round(freq)     | Round datetime              | s.dt.round("H")                     |
| s.dt.floor(freq)     | Floor datetime              | s.dt.floor("D")                     |
| s.dt.ceil(freq)      | Ceil datetime               | s.dt.ceil("D")                      |

## Extracting rows as `DataFrame`

```python
# Get data in row
monday_data = data[data.day == "Monday"]

print(monday_data)  # still a DataFrame
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

data_dict = {"students": ["Amy", "Wine", "House"], "scores": [90, 80, 70]}
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

student_dict = {"students": ["Amy", "Wine", "House"], "scores": [90, 80, 70]}

student_pd = pd.DataFrame(student_dict)

for (key, value) in student_pd.items():
    print(value)(0, 90)(1, 80)(2, 70)
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
    print(f"Student:{row.students}")  # row is a Series
```

```python
Index: 0
Row: students
Amy
scores
90
Name: 0, dtype: object
Index: 1
Row: students
Wine
scores
80
Name: 1, dtype: object
Index: 2
Row: students
House
scores
70
Name: 2, dtype: object
```

## Grouping and Pivoting Data

We can group columns

```python
df.groupby('ColName').count()
```
Every row column will have the same value with the count

This gives the mean mid career salary per group

```python
clean_df.groupby('Group')['Mid-Career Median Salary'].mean()
```
