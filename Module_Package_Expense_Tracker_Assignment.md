
# 📝 Assignment: Personal Expense Tracker using Python Modules and Packages

## 🎯 Objective
Create a modular and well-structured Python application using **modules and packages** to manage daily personal expenses. The user should be able to add, view, filter, and summarize expenses.

---

## 📁 Folder Structure

```
expense_tracker/
│
├── __init__.py
├── add_expense.py
├── report.py
├── summary.py
└── main.py
```

---

## ✅ Functional Requirements

### 🔹 `add_expense.py`
Defines a function to add an expense record.

```python
def add_expense(expenses, date, category, amount, description):
    expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    })
```

---

### 🔹 `report.py`
Provides functions to display and filter expenses.

```python
def show_all(expenses):
    for exp in expenses:
        print(exp)

def filter_by_category(expenses, category):
    return [e for e in expenses if e["category"] == category]
```

---

### 🔹 `summary.py`
Provides functions to calculate summaries of expenses.

```python
def total_expense(expenses):
    return sum(e["amount"] for e in expenses)

def expense_by_category(expenses):
    summary = {}
    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]
    return summary
```

---

### 🔹 `main.py`
Acts as the entry point for the application and provides a menu-driven interface.

```python
from expense_tracker import add_expense, report, summary

expenses = []

while True:
    print("\n1. Add Expense\n2. View All\n3. Filter by Category\n4. Show Total\n5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        date = input("Date (YYYY-MM-DD): ")
        cat = input("Category: ")
        amt = float(input("Amount: "))
        desc = input("Description: ")
        add_expense.add_expense(expenses, date, cat, amt, desc)

    elif choice == '2':
        report.show_all(expenses)

    elif choice == '3':
        cat = input("Category: ")
        filtered = report.filter_by_category(expenses, cat)
        report.show_all(filtered)

    elif choice == '4':
        print("Total Spent:", summary.total_expense(expenses))
        print("By Category:", summary.expense_by_category(expenses))

    elif choice == '5':
        break
```

---

## 💡 Bonus Suggestions
- Export and import data to/from CSV files
- Visualize expenses by category using charts
- Monthly expense summary view
- Add validations and error handling

---

## 📌 Learning Outcomes
- Learn how to use **modules** and **packages** in Python
- Understand code organization in a real-world utility
- Improve Python fundamentals with hands-on practice
