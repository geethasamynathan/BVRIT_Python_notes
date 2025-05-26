
# Advanced Python Comprehensions with Real-World Scenarios

## ✅ What are Comprehensions?

Comprehensions offer **shorter syntax** for creating new sequences (lists, tuples, dicts, sets) by **iterating over iterables** and optionally **filtering elements**.

---

## 1. List Comprehension

### 📌 Real-world Scenario: Filtering active users’ names
```python
users = [("Alice", True), ("Bob", False), ("Charlie", True)]

# Using list comprehension
active_users = [name for name, status in users if status]
print(active_users)  # ['Alice', 'Charlie']
```

### ❌ Without Comprehension:
```python
active_users = []
for name, status in users:
    if status:
        active_users.append(name)
```

---

## 2. Tuple Comprehension (via generator expression)

### 📌 Real-world Scenario: Uppercasing product codes
```python
product_codes = ["abc123", "xyz987", "def456"]
upper_codes = tuple(code.upper() for code in product_codes)
print(upper_codes)  # ('ABC123', 'XYZ987', 'DEF456')
```

### ❌ Without Comprehension:
```python
upper_codes = []
for code in product_codes:
    upper_codes.append(code.upper())
upper_codes = tuple(upper_codes)
```

---

## 3. Dictionary Comprehension

### 📌 Real-world Scenario: Mapping student names to marks (>=50)
```python
marks = {"Alice": 82, "Bob": 43, "Charlie": 55}
passed = {name: score for name, score in marks.items() if score >= 50}
print(passed)  # {'Alice': 82, 'Charlie': 55}
```

### ❌ Without Comprehension:
```python
passed = {}
for name, score in marks.items():
    if score >= 50:
        passed[name] = score
```

---

## 4. Set Comprehension

### 📌 Real-world Scenario: Extracting unique departments
```python
employees = [("Alice", "IT"), ("Bob", "HR"), ("Charlie", "IT"), ("David", "Finance")]
departments = {dept for _, dept in employees}
print(departments)  # {'Finance', 'HR', 'IT'}
```

### ❌ Without Comprehension:
```python
departments = set()
for _, dept in employees:
    departments.add(dept)
```

---

## 🔍 Functional Comparisons

| Type       | With Comprehension (Code Length) | Without Comprehension (Code Length) | Clarity        | Performance |
|------------|----------------------------------|--------------------------------------|----------------|-------------|
| List       | 1 line                           | 4–5 lines                            | High           | Faster      |
| Tuple      | 1 line                           | 4–5 lines                            | High           | Efficient   |
| Dictionary | 1 line                           | 4–6 lines                            | High           | Faster      |
| Set        | 1 line                           | 3–4 lines                            | High           | Faster      |

---

## 🧠 Summary

| Comprehension | Purpose                         | Syntax Example                                  |
|---------------|----------------------------------|-------------------------------------------------|
| List          | Filter/transform lists           | `[x for x in lst if x > 10]`                    |
| Tuple         | Create tuples via generators     | `tuple(x for x in lst)`                         |
| Dict          | Create dict with logic           | `{k:v for k,v in d.items() if v>10}`            |
| Set           | Extract unique values            | `{x for x in lst if x != ""}`                   |

---

## 📌 Advanced Tips

- **Nested Comprehensions**:
  ```python
  matrix = [[1, 2], [3, 4]]
  flattened = [num for row in matrix for num in row]  # [1, 2, 3, 4]
  ```

- **Conditional Expressions**:
  ```python
  result = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
  ```

---
