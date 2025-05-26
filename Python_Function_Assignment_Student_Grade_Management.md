
# 🧑‍🎓 Real-World Python Assignment: Student Grade Management System

## 🎯 Objective
Build a student grade management system using the following Python concepts:
- List of dictionaries
- Function with required arguments, *args, **kwargs
- Function decorator
- Loops and control statements
- **No object-oriented programming**

---

## 🔧 Requirements

1. Use a **decorator** to log function activity.
2. Use a function to **add student data** using `*args` and `**kwargs`.
3. Store student records in a **list of dictionaries**.
4. Use **loops and conditionals** to calculate and display results.
5. Avoid using classes (OOP is not allowed).

---

## ✅ Solution Code

```python
import datetime

# Decorator to log activity
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[{datetime.datetime.now()}] Executing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# List of dictionaries to hold student data
students = []

# Function to add students
@log_action
def add_student(name, *scores, **meta):
    average = sum(scores) / len(scores)
    status = "Pass" if average >= 40 else "Fail"

    student = {
        "name": name,
        "scores": scores,
        "average": average,
        "status": status,
        "metadata": meta
    }

    students.append(student)

# Function to display all student data
@log_action
def display_students():
    for student in students:
        print(f"\nStudent: {student['name']}")
        print(f"Scores: {student['scores']}")
        print(f"Average: {student['average']:.2f}")
        print(f"Status: {student['status']}")
        if student['metadata']:
            print("Additional Info:")
            for key, value in student['metadata'].items():
                print(f" - {key}: {value}")

# Add students
add_student("Alice", 78, 85, 92, city="Bangalore", age=17)
add_student("Bob", 35, 40, 38, city="Mumbai", scholarship="No")
add_student("Charlie", 55, 60, 58)

# Display all student records
display_students()
```

---

## 🔍 Explanation by Component

### ✅ Decorator
```python
def log_action(func):
    ...
```
Adds timestamp logging to any function it's applied to.

---

### ✅ List of Dictionaries
```python
students = []
```
Holds multiple student records, each stored as a dictionary.

---

### ✅ Function with `*args` and `**kwargs`
```python
def add_student(name, *scores, **meta):
```
- `name`: required argument
- `*scores`: collects subject marks
- `**meta`: captures extra data like city, age

---

### ✅ Control Statement
```python
status = "Pass" if average >= 40 else "Fail"
```
Checks if the student passed based on average score.

---

### ✅ Loop
```python
for student in students:
```
Iterates through each student and prints their details.

---

## 📦 Sample Output

```
[2025-05-25 11:30:45.567890] Executing: add_student
[2025-05-25 11:30:45.567891] Executing: add_student
[2025-05-25 11:30:45.567892] Executing: add_student
[2025-05-25 11:30:45.567893] Executing: display_students

Student: Alice
Scores: (78, 85, 92)
Average: 85.00
Status: Pass
Additional Info:
 - city: Bangalore
 - age: 17

Student: Bob
Scores: (35, 40, 38)
Average: 37.67
Status: Fail
Additional Info:
 - city: Mumbai
 - scholarship: No

Student: Charlie
Scores: (55, 60, 58)
Average: 57.67
Status: Pass
```
