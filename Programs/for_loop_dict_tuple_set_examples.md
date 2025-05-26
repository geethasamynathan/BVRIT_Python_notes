# Python `for` Loop Examples: Dictionary, Tuple, and Set

---

## ✅ 1. Looping through a Dictionary (key-value pairs)

```python
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Loop over keys
for key in person:
    print("Key:", key)

# Loop over values
for value in person.values():
    print("Value:", value)

# Loop over key-value pairs
for key, value in person.items():
    print(f"{key} => {value}")
```

---

## ✅ 2. Looping through a Tuple

```python
coordinates = (12.34, 56.78, 90.12)

for value in coordinates:
    print("Coordinate value:", value)
```

Use case: GPS coordinates, immutable data

---

## ✅ 3. Looping through a Set

```python
unique_items = {"apple", "banana", "cherry"}

for item in unique_items:
    print("Fruit:", item)
```

Note: Sets are **unordered**, so the output order may vary.

---

## ✅ Bonus: Nested Dictionary Looping

```python
inventory = {
    "Pens": {"price": 5, "stock": 100},
    "Notebooks": {"price": 20, "stock": 200}
}

for item, details in inventory.items():
    print(f"Item: {item}")
    for key, value in details.items():
        print(f"  {key}: {value}")
```