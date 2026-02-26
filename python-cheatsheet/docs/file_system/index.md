# 🐍 Working with file system

## Simple read and write

```python
my_file = open("my_file.txt")
file_content = my_file.read()
print(file_content)
my_file.close() #to release the resources
```

## Self close file using `with`

```python
with open("my_file.txt") as my_file:
    file_content = my_file.read()   
    print(file_content)
```

------------------------------------------------------------------------

## File Modes

  Mode    Description
  ------- ---------------------
  `"r"`   Read
  `"w"`   Write (overwrites)
  `"a"`   Append
  `"x"`   Create new file
  `"b"`   Binary mode
  `"t"`   Text mode (default)

Example:

``` python
with open("file.txt", "w") as f:
    f.write("Hello")
```

------------------------------------------------------------------------

## Reading Files

``` python
with open("file.txt", "r") as f:
    print(f.read())
```

Read line by line:

``` python
with open("file.txt") as f:
    for line in f:
        print(line.strip())
```

Read all lines at once

```python
file_name = "file.txt"
lines = ["First line\n", "Second line\n", "Third line\n"]

with open(file=file_name, mode="w") as f:
    f.writelines(lines)

with open("file.txt") as f:
    line_list = f.readlines()

for line in line_list:
    print("Line:",line)
```

------------------------------------------------------------------------

## Writing Files

``` python
with open("file.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")
```

Append:

``` python
with open("file.txt", "a") as f:
    f.write("New line\n")
```

------------------------------------------------------------------------

## Absolute path

Independently of the OS being used the absolute path always starts with `/`

No `MacintoshHd` (for Mac) or `c:/` (for Windows) is needed

------------------------------------------------------------------------

## Working with Directories (os module)

### Get current directory

``` python
import os

print(os.getcwd())
```

### List directory contents

``` python
print(os.listdir("."))
```

### Create directory

``` python
os.mkdir("new_folder")
```

Create nested directories:

``` python
os.makedirs("parent/child")
```

### Remove directory

``` python
os.rmdir("new_folder")
```

------------------------------------------------------------------------

## Modern Approach: pathlib (Recommended)

``` python
from pathlib import Path
```

### Create Path object

``` python
path = Path("example.txt")
```

### Check if file exists

``` python
print(path.exists())
```

### Check if file or directory

``` python
print(path.is_file())
print(path.is_dir())
```

### Create directory

``` python
Path("new_folder").mkdir()
```

### Create nested directories

``` python
Path("parent/child").mkdir(parents=True, exist_ok=True)
```

------------------------------------------------------------------------

## Reading and Writing with pathlib

### Write text

``` python
path = Path("file.txt")
path.write_text("Hello World")
```

### Read text

``` python
content = path.read_text()
print(content)
```

------------------------------------------------------------------------

### Listing Files

``` python
from pathlib import Path

for file in Path(".").iterdir():
    print(file)
```

Only Python files:

``` python
for file in Path(".").glob("*.py"):
    print(file)
```

------------------------------------------------------------------------

### File Information

``` python
path = Path("file.txt")

print(path.name)
print(path.suffix)
print(path.stem)
print(path.stat().st_size)
```

------------------------------------------------------------------------

### Copy and Move Files

``` python
import shutil

shutil.copy("file.txt", "copy.txt")
shutil.move("copy.txt", "folder/copy.txt")
```

------------------------------------------------------------------------

### Delete Files

``` python
Path("file.txt").unlink()
```

------------------------------------------------------------------------

## Best Practices

-   Always use `with open()`
-   Prefer `pathlib` over `os`
-   Handle exceptions
-   Use absolute paths when needed

Example:

``` python
try:
    content = Path("file.txt").read_text()
except FileNotFoundError:
    print("File not found")
```

------------------------------------------------------------------------

# Recommended Modern Pattern

``` python
from pathlib import Path

path = Path("data.txt")

if path.exists():
    print(path.read_text())
else:
    path.write_text("New file created")
```
