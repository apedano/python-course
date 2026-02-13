# 🐍 Python Modules

## 📌 What is a Python Module?

A **module** is simply a `.py` file that contains Python code: -
Variables - Functions - Classes - Lists or other data structures

Modules help you: - Organize code - Reuse functionality - Keep projects
clean and maintainable

------------------------------------------------------------------------

# 📁 Basic Example

## Project Structure

    project/
    │
    ├── data.py
    └── main.py

------------------------------------------------------------------------

## 🗂 data.py

``` python
# data.py

names = ["Alice", "Bob", "Charlie", "Diana"]
```

Here we define a **list of strings** in a separate file.

------------------------------------------------------------------------

# 📥 Importing a List from Another File

## ✅ Option 1 -- Import the Variable Directly (Recommended)

``` python
from data import names

print(names)
```

✔ Cleaner syntax\
✔ Best when importing specific items

------------------------------------------------------------------------

## ✅ Option 2 -- Import the Entire Module

``` python
import data

print(data.names)
```

✔ Better for larger modules\
✔ Makes origin of variable explicit

------------------------------------------------------------------------

# 📦 How Imports Work

When you write:

``` python
import data
```

Python: 1. Searches for `data.py` 2. Loads it as a module 3. Makes its
contents available

------------------------------------------------------------------------

# 📂 Importing from Subfolders (Packages)

## Structure

    project/
    │
    ├── utils/
    │   ├── __init__.py
    │   └── data.py
    └── main.py

## Import Statement

``` python
from utils.data import names
```

The `__init__.py` file tells Python that `utils` is a package.

------------------------------------------------------------------------

# 🚨 Common Mistakes

## ❌ Including `.py` in import

Wrong:

``` python
from data.py import names
```

Correct:

``` python
from data import names
```

------------------------------------------------------------------------

## ❌ Files not in the same folder

If modules are in different directories: - Use packages
(`__init__.py`) - Adjust PYTHONPATH - Use proper package structure

------------------------------------------------------------------------

# 🔎 Debug Tip

To see where a module is loaded from:

``` python
import data
print(data.__file__)
```

------------------------------------------------------------------------

# 🧠 Best Practices

-   Keep modules small and focused
-   Use descriptive module names
-   Avoid circular imports
-   Group related functionality together

------------------------------------------------------------------------

# ✅ Summary

-   A module is a `.py` file
-   Use `from module import variable` for specific imports
-   Use `import module` for full access
-   Use packages for larger projects
