
# 📦 Module and Package in Python

---

## 🔹 MODULE in Python

A **module** is simply a Python file (`.py`) that contains **functions**, **classes**, and **variables** you can reuse in other Python scripts.

### ✅ Why use a module?
- Helps organize your code
- Allows reuse of functions and logic
- Makes large projects more manageable

### 🛠 Real-world Analogy:
Think of a **module** like a tool in a toolbox. You open the toolbox (your code) and pick the tool (module) you need.

---

### ✅ Example of a Module

Let's create a file named `math_utils.py`:

```python
# math_utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

Now in another file, you can import and use this:

```python
# app.py
import math_utils

result = math_utils.add(10, 5)
print("Sum:", result)
```

---

## 🔹 PACKAGE in Python

A **package** is a **collection of modules** organized in a directory with a special `__init__.py` file (can be empty) that tells Python it’s a package.

### ✅ Why use a package?
- Helps structure larger projects
- Organizes related modules under one namespace

### 🛠 Real-world Analogy:
A **package** is like a folder of tools (modules). For example, a folder named "FinanceTools" might have `tax.py`, `budget.py`, and `invoice.py`.

---

### ✅ Example of a Package

**Folder Structure:**
```
finance/
│
├── __init__.py
├── tax.py
└── budget.py
```

**`tax.py`**
```python
def calculate_tax(amount):
    return amount * 0.18
```

**`budget.py`**
```python
def create_budget(income, expenses):
    return income - expenses
```

**Main Script `main.py`**
```python
from finance import tax, budget

print("Tax:", tax.calculate_tax(10000))
print("Remaining:", budget.create_budget(50000, 30000))
```

---

## ✅ Summary Table

| Feature         | Module                          | Package                                  |
|----------------|----------------------------------|------------------------------------------|
| Definition      | Single `.py` file               | Folder with `__init__.py` + modules      |
| Use             | Reuse code                      | Organize multiple modules                |
| Example         | `math_utils.py`                 | `finance/` with `tax.py`, `budget.py`    |
| Import Syntax   | `import math_utils`             | `from finance import tax`                |

---
