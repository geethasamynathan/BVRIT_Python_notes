# Real-World Examples of `for` Loop with Lists in Python

## 1. Basic Iteration
Iterate over a list of products and print each name.

```python
products = ["Laptop", "Phone", "Tablet", "Monitor"]
for item in products:
    print("Product:", item)
```

---

## 2. Using `enumerate()`
Get both the index and the value.

```python
products = ["Laptop", "Phone", "Tablet"]
for index, item in enumerate(products):
    print(f"{index + 1}. {item}")
```

---

## 3. Conditional Filtering in Loop
Print only items costing more than $500.

```python
prices = [1200, 300, 850, 150]
for price in prices:
    if price > 500:
        print("Expensive item:", price)
```

---

## 4. List of Dictionaries
Iterate through user data.

```python
users = [
    {"name": "Alice", "role": "Admin"},
    {"name": "Bob", "role": "User"},
    {"name": "Charlie", "role": "Moderator"},
]

for user in users:
    print(f"{user['name']} is a {user['role']}")
```

---

## 5. Using `range()` with Index
Useful when index math is needed.

```python
scores = [85, 92, 78, 90]
for i in range(len(scores)):
    print(f"Student {i + 1} scored {scores[i]}")
```

---

## 6. Nested `for` Loops
Matrix traversal (2D lists).

```python
sales = [
    [200, 300, 250],
    [400, 150, 100],
    [100, 120, 110]
]

for row in sales:
    for amount in row:
        print("Amount:", amount)
```

---

## 7. List Comprehension (Alternative to `for`)
Create a new list of discounted prices.

```python
prices = [100, 200, 300]
discounted = [p * 0.9 for p in prices]
print(discounted)  # [90.0, 180.0, 270.0]
```

---

## 8. Using `zip()` with Two Lists
Combining names and scores.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")
```

---

## 9. Break/Continue with Loop
Skip blacklisted products.

```python
products = ["Laptop", "Phone", "BannedItem", "Tablet"]
for item in products:
    if item == "BannedItem":
        continue  # skip this item
    print("Processing:", item)
```

---

## 10. Reverse Iteration
Print elements in reverse order.

```python
cities = ["Delhi", "Mumbai", "Bangalore"]
for city in reversed(cities):
    print(city)
```

---

## 11. Loop with `else` Clause
Check if a product exists.

```python
products = ["Pen", "Pencil", "Notebook"]
for p in products:
    if p == "Marker":
        print("Found Marker")
        break
else:
    print("Marker not found")
```

---


