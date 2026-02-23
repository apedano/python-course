# 🐍 Package

way larger than modules

## Import a package - PyPI Python Package Index

Website: https://pypi.org/

Sample package: https://pypi.org/project/prettytable/

## Installation

### Ensuere `pip` is executable

The package manager is installed together with the virtual environment

```bash
python3 -m pip --version
```

### Install a package 

```shell
python3 -m pip install -U prettytable
```

### Use a package

```python
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
...

print(table)
```



