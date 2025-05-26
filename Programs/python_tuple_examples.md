# ✅ Real-World Examples of Python Tuples and Their Methods

---

## 🔹 What is a Tuple?

A **tuple** is an ordered, immutable collection of elements. You can think of it as a list you cannot modify.

```python
location = ("New York", 40.7128, -74.0060)
```

---

## ✅ Real-World Examples and Use Cases

### 1. Returning Multiple Values from a Function

```python
def get_employee():
    return ("Alice", "Developer", 85000)

name, role, salary = get_employee()
print(name, role, salary)
```

---

### 2. Using Tuple in Dictionaries (like a coordinate system)

```python
locations = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles"
}

print(locations[(40.7128, -74.0060)])  # Output: New York
```

---

### 3. Immutability for Safety

```python
credentials = ("admin", "secret123")
# credentials[0] = "user"  # ❌ Error: Tuples are immutable
```

---

## ✅ Tuple Methods

### 1. `count()`: Count how many times an item appears

```python
colors = ("red", "blue", "green", "red", "yellow")
print(colors.count("red"))  # Output: 2
```

---

### 2. `index()`: Find the first index of an item

```python
colors = ("red", "blue", "green", "red")
print(colors.index("green"))  # Output: 2
```

---

## ✅ Other Common Operations

### 1. Tuple Packing and Unpacking

```python
person = ("Alice", 30, "Engineer")
name, age, job = person
print(name, age, job)
```

---

### 2. Iterating Over a Tuple

```python
for item in ("pen", "notebook", "eraser"):
    print("Item:", item)
```

---

### 3. Nested Tuples

```python
team = (("John", "Dev"), ("Jane", "Manager"))
for member in team:
    print(f"{member[0]} is a {member[1]}")
```

---

### 4. Tuples as Dictionary Keys

```python
stock_prices = {
    ("AAPL", "2025-05-22"): 185.67,
    ("GOOGL", "2025-05-22"): 2701.35
}
print(stock_prices[("AAPL", "2025-05-22")])
```

---

Tuples are excellent for fixed-size, immutable data and are commonly used in data science, configuration, and multi-value function returns.