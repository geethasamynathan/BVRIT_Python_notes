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
        entry = f"{expense['date']} - {expense['item']} - ₹{expense['amount']}
"
        file.write(entry)

# Reading back the file using 'r'
print("📋 All Expense Entries:")
with open("expenses.txt", "r") as file:
    print(file.read())

# Overwriting with summary using writelines()
summary = [
    "\nSummary as of " + str(datetime.now()) + "\n",
    "Total Items: {}
".format(len(expenses)),
    "Total Spent: ₹{}
".format(sum([e["amount"] for e in expenses]))
]

with open("expenses_summary.txt", "w") as file:
    file.writelines(summary)
