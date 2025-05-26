
# 🧾 Real-World Python Assignment: Employee Expense Tracker (No OOP)

## 🎯 Objective:
Build an expense tracking system for employees using:
- ✅ List of dictionaries  
- ✅ Function with required args, `*args`, `**kwargs`  
- ✅ Function decorators for audit logging  
- ✅ Loops and control statements  
- ❌ No OOP allowed  

---

## 🧠 Scenario:
You're managing employee travel expenses. Each entry should capture:
- Employee Name  
- Any number of expenses (travel, food, lodging, etc.)  
- Extra info like location and department (via `**kwargs`)  
- Calculate total and validate whether it exceeds the company's daily budget  

---

## ✅ Requirements:

1. Use a **decorator** to log every operation.
2. Add employee expenses using `*args` and `**kwargs`.
3. Store all data in a **list of dictionaries**.
4. Use loops and conditions to:
   - Print all expenses
   - Show whether it’s under budget or over budget (₹2000/day)

---

## ✅ Solution Code

```python
import datetime

# Step 1: Logging decorator
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[{datetime.datetime.now()}] Function called: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Step 2: Main data storage
expenses = []

# Step 3: Add expense function
@log_action
def add_expense(employee_name, *amounts, **details):
    total = sum(amounts)
    status = "Under Budget" if total <= 2000 else "Over Budget"

    record = {
        "employee": employee_name,
        "expenses": amounts,
        "total": total,
        "status": status,
        "details": details
    }
    expenses.append(record)

# Step 4: Display all expenses
@log_action
def show_expenses():
    for e in expenses:
        print(f"\nEmployee: {e['employee']}")
        print(f"Expenses: {e['expenses']}")
        print(f"Total: ₹{e['total']}")
        print(f"Status: {e['status']}")
        if e['details']:
            print("Additional Info:")
            for k, v in e['details'].items():
                print(f" - {k}: {v}")

# Step 5: Add sample data
add_expense("Arun", 500, 800, 600, location="Delhi", department="IT")
add_expense("Rita", 1000, 1200, location="Mumbai", purpose="Client Meeting")
add_expense("John", 300, 400, 350, department="HR")

# Step 6: Show report
show_expenses()
```

---

## 🔍 Breakdown of Key Concepts

| Concept                 | Where Used                                                   |
|-------------------------|--------------------------------------------------------------|
| **Decorator**           | `log_action` logs every function call                        |
| **List of Dictionaries**| `expenses` holds all employee records                        |
| **Function with *args** | Captures unlimited expenses like travel, food, lodging       |
| **Function with **kwargs** | Captures extra details like department, location           |
| **Loop + Condition**    | Loop through records and check if total exceeds ₹2000/day    |

---

## 📦 Sample Output

```
[2025-05-25 11:45:00] Function called: add_expense
[2025-05-25 11:45:00] Function called: add_expense
[2025-05-25 11:45:00] Function called: add_expense
[2025-05-25 11:45:00] Function called: show_expenses

Employee: Arun
Expenses: (500, 800, 600)
Total: ₹1900
Status: Under Budget
Additional Info:
 - location: Delhi
 - department: IT

Employee: Rita
Expenses: (1000, 1200)
Total: ₹2200
Status: Over Budget
Additional Info:
 - location: Mumbai
 - purpose: Client Meeting

Employee: John
Expenses: (300, 400, 350)
Total: ₹1050
Status: Under Budget
Additional Info:
 - department: HR
```
