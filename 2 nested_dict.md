
# 🧩 Python Nested Dictionary – Real-World Scenarios with Examples

A **nested dictionary** is a dictionary inside another dictionary. It’s useful for representing **complex structured data**, such as JSON responses, databases, or config files.

---

## 🔹 Syntax

```python
nested_dict = {
    "outer_key1": {"inner_key1": "value1", "inner_key2": "value2"},
    "outer_key2": {"inner_key1": "value3", "inner_key2": "value4"}
}
```

---

## ✅ Scenario 1: Employee Database

### 🧾 Dictionary Structure

```python
employees = {
    "E001": {"name": "Alice", "department": "HR", "salary": 50000},
    "E002": {"name": "Bob", "department": "IT", "salary": 60000},
    "E003": {"name": "Charlie", "department": "Finance", "salary": 55000}
}
```

### ❓ Questions and Solutions

#### 1. Get salary of employee E002

```python
print(employees["E002"]["salary"])  # Output: 60000
```

#### 2. Add a new employee

```python
employees["E004"] = {"name": "David", "department": "Marketing", "salary": 52000}
```

#### 3. Update department of Charlie

```python
employees["E003"]["department"] = "IT"
```

#### 4. List all employee names and departments

```python
for emp_id, details in employees.items():
    print(f"{emp_id}: {details['name']} - {details['department']}")
```

#### 5. Find total salary expense

```python
total_salary = sum(emp["salary"] for emp in employees.values())
print("Total Salary:", total_salary)
```

---

## ✅ Scenario 2: Product Inventory System

```python
inventory = {
    "P001": {"name": "Laptop", "stock": 10, "price": 75000},
    "P002": {"name": "Mouse", "stock": 50, "price": 500},
    "P003": {"name": "Keyboard", "stock": 30, "price": 1000}
}
```

### ❓ Questions and Solutions

#### 1. List products with stock < 20

```python
low_stock = [v['name'] for v in inventory.values() if v['stock'] < 20]
print("Low stock items:", low_stock)
```

#### 2. Calculate inventory value

```python
total_value = sum(item["stock"] * item["price"] for item in inventory.values())
print("Total Inventory Value:", total_value)
```

#### 3. Update stock after sale of 2 keyboards

```python
inventory["P003"]["stock"] -= 2
```

#### 4. Add a new product

```python
inventory["P004"] = {"name": "Monitor", "stock": 15, "price": 12000}
```

---

## ✅ Scenario 3: School Grading System

```python
grades = {
    "John": {"Math": 90, "Science": 85},
    "Emma": {"Math": 78, "Science": 92},
    "Liam": {"Math": 88, "Science": 80}
}
```

### ❓ Questions and Solutions

#### 1. Add a new subject (English) for all students

```python
for student in grades:
    grades[student]["English"] = 0  # default marks
```

#### 2. Update John's English marks

```python
grades["John"]["English"] = 95
```

#### 3. Calculate average score for each student

```python
for student, subjects in grades.items():
    avg = sum(subjects.values()) / len(subjects)
    print(f"{student} - Average: {avg:.2f}")
```

---

## 🔸 When to Use Nested Dictionaries

- **Structured configurations** (e.g., app settings)
- **JSON-style API data**
- **Multi-attribute records** (users, products, students)
- **Dynamic key grouping** (e.g., logs by user, date, category)

---

## 🧠 Summary

| Use Case              | Example Structure                  |
|------------------------|------------------------------------|
| Employee Records       | `{id: {name, department, salary}}` |
| Product Inventory      | `{pid: {name, stock, price}}`      |
| Student Grades         | `{name: {subject: mark}}`          |
| App Configs            | `{section: {setting: value}}`      |

Nested dictionaries are a powerful way to manage complex data hierarchies in a readable and maintainable way.
