
# 🔹 Lambda Function in Python

A **lambda function** in Python is a small **anonymous function** — meaning it **doesn't have a name**. It's often used for **short, throwaway functions** that are created on the fly, typically passed as arguments to higher-order functions like `map()`, `filter()`, `sorted()`, etc.

---

## ✅ Syntax:
```python
lambda arguments: expression
```

- You can have **multiple arguments** but only **one expression**.
- It **automatically returns** the result of the expression (no `return` keyword needed).

---

## 🧠 Equivalent to:
```python
def add(x, y):
    return x + y

# is same as
lambda x, y: x + y
```

---

## 📌 Real-World Examples

### 1. Sorting a List of Tuples by Second Value
```python
data = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # [('Bob', 20), ('Alice', 25), ('Charlie', 30)]
```

---

### 2. Using with `map()` to Square Numbers
```python
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # [1, 4, 9, 16]
```

---

### 3. Using with `filter()` to Get Even Numbers
```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6]
```

---

### 4. With `reduce()` to Calculate Factorial
```python
from functools import reduce
factorial = reduce(lambda x, y: x * y, range(1, 6))
print(factorial)  # 120 (5!)
```

---

## 🔍 When to Use Lambda Functions

| Use Case                    | Lambda Recommended? | Example                    |
|----------------------------|---------------------|----------------------------|
| One-liner transformation   | ✅ Yes              | With `map()` or `sorted()` |
| Reuse or multiple lines    | ❌ No               | Use `def` instead          |
| Readability is key         | ❌ No               | Named functions are better |

---

## ❗ Caution:
- Avoid overusing lambda for **complex logic**.
- It should be used **for clarity**, not as a shortcut.

---
