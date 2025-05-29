# 💡write and read  in Python

Let us demonstrates how to write to files using various Python file writing methods (`write()`, `writelines()`, `read()`) 

---

## 🎯 Use Case: Daily Expense Tracker

**Goal**: Log daily expenses in a file and summarize the results.

---

### 📁 Files:
- `expenses.txt` – Appends each new entry.
- `expenses_summary.txt` – Overwrites with a summary report.

---

### ✅ Python Code

```python
from datetime import datetime

# Sample expense entries
expenses = [
    {"date": "2025-05-27", "item": "Groceries", "amount": 450},
    {"date": "2025-05-27", "item": "Petrol", "amount": 1200},
    {"date": "2025-05-27", "item": "Coffee", "amount": 150}
]

# Writing expense entries using append mode with write()
with open("expenses.txt", "a") as file:
    for expense in expenses:
        entry = f"{expense['date']} - {expense['item']} - ₹{expense['amount']}\n"
        file.write(entry)

# Reading back the file using 'r'
print("📋 All Expense Entries:")
with open("expenses.txt", "r") as file:
    print(file.read())

# Overwriting with summary using writelines()
summary = [
    "\nSummary as of " + str(datetime.now()) + "\n",
    "Total Items: {}\n".format(len(expenses)),
    "Total Spent: ₹{}\n".format(sum([e["amount"] for e in expenses]))
]

with open("expenses_summary.txt", "w") as file:
    file.writelines(summary)
```

---

## 📝 Example Output

### `expenses.txt`
```
2025-05-27 - Groceries - ₹450
2025-05-27 - Petrol - ₹1200
2025-05-27 - Coffee - ₹150
```

### `expenses_summary.txt`
```
Summary as of 2025-05-27 04:08:41
Total Items: 3
Total Spent: ₹1800
```

---

### 📌 Methods Used:

| Method         | File Mode | Description                               |
|----------------|-----------|-------------------------------------------|
| `write()`      | `"a"`     | Append new entries                        |
| `writelines()` | `"w"`     | Write multiple summary lines at once     |
| `read()`       | `"r"`     | Display file content                      |
