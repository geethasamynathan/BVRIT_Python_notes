# 📝 Python List-Based Assignments with `if`, `elif`, and `for` – With Solutions

---

## ✅ Assignment 1: Student Grader

**Problem:**  
Given a list of student marks, assign grades using the following logic:
- `>= 90`: Grade A
- `>= 75`: Grade B
- `>= 60`: Grade C
- `< 60`: Grade F

**Input:**
```python
marks = [95, 82, 67, 45, 88]
```

**Solution:**
```python
marks = [95, 82, 67, 45, 88]

for mark in marks:
    if mark >= 90:
        grade = 'A'
    elif mark >= 75:
        grade = 'B'
    elif mark >= 60:
        grade = 'C'
    else:
        grade = 'F'
    print(f"Mark: {mark}, Grade: {grade}")
```

---

## ✅ Assignment 2: Grocery Price Checker

**Problem:**  
Categorize items as essential, junk, or neutral.

**Input:**
```python
items = ["milk", "chips", "banana", "bread", "soda", "rice"]
```

**Solution:**
```python
items = ["milk", "chips", "banana", "bread", "soda", "rice"]

for item in items:
    if item in ["milk", "bread"]:
        category = "Essential"
    elif item in ["chips", "soda"]:
        category = "Junk"
    else:
        category = "Neutral"
    print(f"{item.title()} is {category}")
```

---

## ✅ Assignment 3: City Temperature Report

**Problem:**  
Label each city based on temperature as Hot, Moderate, or Cold.

**Input:**
```python
city_temperatures = [("Delhi", 42), ("Bangalore", 28), ("Shimla", 15), ("Mumbai", 32), ("Chennai", 30)]
```

**Solution:**
```python
city_temperatures = [("Delhi", 42), ("Bangalore", 28), ("Shimla", 15), ("Mumbai", 32), ("Chennai", 30)]

for city, temp in city_temperatures:
    if temp > 30:
        status = "Hot"
    elif temp >= 20:
        status = "Moderate"
    else:
        status = "Cold"
    print(f"{city} is {status} with {temp}°C")
```

---

## ✅ Assignment 4: Find Even, Odd, and Divisible by 5

**Problem:**  
Categorize numbers based on properties.

**Input:**
```python
numbers = [12, 15, 22, 35, 40, 7, 9]
```

**Solution:**
```python
numbers = [12, 15, 22, 35, 40, 7, 9]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is Even", end=", ")
    else:
        print(f"{num} is Odd", end=", ")

    if num % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")
```

---

## ✅ Assignment 5: Voter Eligibility by Age Group

**Problem:**  
Determine voter eligibility by age.

**Input:**
```python
people = [("Alice", 17), ("Bob", 21), ("Charlie", 16), ("David", 19)]
```

**Solution:**
```python
people = [("Alice", 17), ("Bob", 21), ("Charlie", 16), ("David", 19)]

for name, age in people:
    if age >= 18:
        print(f"{name} is eligible to vote.")
    else:
        print(f"{name} is not eligible to vote.")
```

---