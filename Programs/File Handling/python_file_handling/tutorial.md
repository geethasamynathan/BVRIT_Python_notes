# 📁 Python File and Directory Operations – Tutorial

This tutorial demonstrates how to handle files and directories in Python with real-world use cases.

---

## ✅ 1. List All Files in a Directory

```python
import os

files = os.listdir(".")
print("All files in current directory:", files)
```

---

## ✅ 2. Create a New File

```python
with open("newfile.txt", "w") as file:
    file.write("This is a newly created file.")
print("File created successfully.")
```

---

## ✅ 3. Check if File Exists

```python
import os

if os.path.exists("newfile.txt"):
    print("File exists.")
else:
    print("File does not exist.")
```

---

## ✅ 4. Rename a File

### 1.
```python
import os

os.rename("newfile.txt", "renamedfile.txt")
print("File renamed.")
```
### ✅ 2. pathlib.Path.rename() – Modern, Object-Oriented
```python
from pathlib import Path

old_path = Path("newfile.txt")
new_path = Path("renamedfile.txt")

old_path.rename(new_path)
print("File renamed using pathlib.")
```
✅ Cleaner syntax

✅ Works with full path objects (Path)

✅ Cross-platform

### 3. shutil.move() – Can Rename and Move
```python
import shutil

shutil.move("newfile.txt", "renamedfile.txt")
print("File renamed using shutil.move.")
✅ If used in the same directory, works like renaming

✅ Can also move to different directories

✅ Handles more edge cases (like copying between filesystems)

## 📌 Summary

| Method           | Rename? | Move Support | Notes                              |
|------------------|---------|--------------|-------------------------------------|
| `os.rename()`    | ✅ Yes  | ❌ No        | Basic rename                        |
| `Path.rename()`  | ✅ Yes  | ❌ No        | Modern, object-oriented             |
| `shutil.move()`  | ✅ Yes  | ✅ Yes       | Rename or move, handles more cases  |

```
---

## ✅ 5. Delete a File

```python
import os

if os.path.exists("renamedfile.txt"):
    os.remove("renamedfile.txt")
    print("File deleted.")
else:
    print("File not found.")
```
## ✅ 1. `os.remove()` – Standard Way

```python
import os

if os.path.exists("file.txt"):
    os.remove("file.txt")
```
✅ Simple and direct

❌ Raises error if file doesn’t exist unless checked manually

### ✅ 2. pathlib.Path.unlink() – Modern and Recommended
```python
from pathlib import Path

file_path = Path("file.txt")

if file_path.exists():
    file_path.unlink()
    print("File deleted using pathlib.")

```
✅ Object-oriented

✅ Cleaner syntax

✅ Preferred in modern Python code

### ✅ 3. os.unlink() – Alias of os.remove()
```python
import os

if os.path.exists("file.txt"):
    os.unlink("file.txt")

```
✅ Exactly same as os.remove()

✅ Slightly more UNIX-style naming

### ✅ 4. try/except for Safe Deletion Without os.path.exists()
```python
try:
    os.remove("file.txt")
    print("File deleted.")
except FileNotFoundError:
    print("File not found.")

```
✅ More Pythonic

✅ Avoids race condition between checking and deleting
---

## ✅ 6. Work with Directories

### Create a Directory
```python
import os

os.makedirs("my_data_folder", exist_ok=True)
print("Directory created.")
```

### Change Working Directory
```python
import os

os.chdir("my_data_folder")
print("Changed working directory to:", os.getcwd())
```

---

## ✅ 7. Read from a CSV File

```python
import csv

with open("sample.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print("Row:", row)
```

---

## ✅ 8. Write to a CSV File

```python
import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "London"],
    ["Charlie", 35, "Sydney"]
]

with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
print("Data written to output.csv.")
```

---

## ✅ Real-World Use Case: Data Archiver Script

Imagine you’re building a script that:
- Reads a CSV report.
- Writes filtered rows to a new file.
- Archives old files by renaming.
- Deletes files older than 30 days.
- Organizes output into a subfolder.

All the techniques above would be part of that real-world script.

---
