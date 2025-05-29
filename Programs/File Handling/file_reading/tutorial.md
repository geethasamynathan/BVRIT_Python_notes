# 📁 File Reading in Python – `read()`, `readline()`, `readlines()`

This tutorial explains how to use `read()`, `readline()`, and `readlines()` in Python for reading file content, with examples and comparisons.

---

## 📄 Sample File Content (`example.txt`)

```
Line 1: Welcome to Python  
Line 2: File handling is simple  
Line 3: Let's learn read methods
```

---

## 1️⃣ `read()` – Read Entire File

### ✅ Description:
- Reads the **entire content** of the file at once.
- Returns a **single string**.

### ✅ Use case:
Use when you want to load the entire file content into memory.

### ✅ Example:

```python
with open("example.txt", "r") as file:
    content = file.read()
    print("Content using read():")
    print(content)
```

---

## 2️⃣ `readline()` – Read One Line at a Time

### ✅ Description:
- Reads the **next line** from the file each time it's called.
- Returns a **string** including the newline (`\n`).

### ✅ Use case:
Useful when reading **line-by-line** from large files (memory-efficient).

### ✅ Example:

```python
with open("example.txt", "r") as file:
    print("Reading line-by-line using readline():")
    print(file.readline())  # Line 1
    print(file.readline())  # Line 2
    print(file.readline())  # Line 3
```

---

## 3️⃣ `readlines()` – Read All Lines as List

### ✅ Description:
- Reads the **entire file** and returns a list where **each line is a list item**.
- Keeps the `\n` at the end of each line.

### ✅ Use case:
Use when you need to **iterate over lines** or process them individually after reading.

### ✅ Example:

```python
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("Lines using readlines():")
    for line in lines:
        print(line.strip())
```

---

## 📊 Differences Summary

| Method        | Reads           | Return Type | Memory Usage | Use Case                           |
|---------------|------------------|-------------|--------------|-------------------------------------|
| `read()`      | Entire file       | `str`        | High          | Small files                         |
| `readline()`  | One line          | `str`        | Low           | Large files, stream processing      |
| `readlines()` | All lines (list)  | `list[str]`  | Medium-High   | Iterating or processing all lines   |

---

## ✅ Real-world Use Case Scenarios

| Scenario                                         | Recommended Method |
|--------------------------------------------------|---------------------|
| Read config or template file (few lines)         | `read()`            |
| Read log file line-by-line for streaming         | `readline()`        |
| Read structured data and parse per line (CSV)    | `readlines()`       |
