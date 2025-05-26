
# 🧑‍💼 Employee Management Python Code – With Explanation

This script manages hardcoded employee data and provides multiple insights like department stats, salary filters, gender count, and more.

---

## 🔸 Hardcoded Employee Dictionary

```python
employees = {
    "E001": {"name": "Alice", "salary": 72000, "location": "Bangalore", "department": "IT", "gender": "Female"},
    "E002": {"name": "Bob", "salary": 45000, "location": "Mumbai", "department": "HR", "gender": "Male"},
    "E003": {"name": "Charlie", "salary": 82000, "location": "Delhi", "department": "Finance", "gender": "Male"},
    "E004": {"name": "Diana", "salary": 52000, "location": "Bangalore", "department": "IT", "gender": "Female"},
    "E005": {"name": "Ethan", "salary": 39000, "location": "Chennai", "department": "Support", "gender": "Male"},
    "E006": {"name": "Fiona", "salary": 61000, "location": "Mumbai", "department": "Finance", "gender": "Female"},
    "E007": {"name": "George", "salary": 47000, "location": "Delhi", "department": "Support", "gender": "Male"},
    "E008": {"name": "Hema", "salary": 95000, "location": "Chennai", "department": "IT", "gender": "Female"}
}
```

---

## 🔹 Display All Employee Details

```python
print("\nEmployee Details:")
for emp_id, emp_info in employees.items():
    print(f"Employee ID: {emp_id}")
    print(f" \n Name: {emp_info['name']}\t Salary: {emp_info['salary']}\t Location: {emp_info['location']}\t Department: {emp_info['department']}\t Gender: {emp_info['gender']}  ")
    print()  # blank line
```
➡️ Loops through each employee and displays their details.

---

## 🔹 Gender-wise Employee Count

```python
gender_count = {"Male": 0, "Female": 0, "Other": 0}
for emp_info in employees.values():
    gender = emp_info["gender"].capitalize()
    if gender in gender_count:
        gender_count[gender] += 1
    else:
        gender_count["Other"] += 1

print("\nGender-wise employee count:")
for gender, count in gender_count.items():
    print(f"  {gender}: {count}")
```
➡️ Tallies total employees by gender, accounting for case sensitivity.

---

## 🔹 Employees with Salary > ₹50,000

```python
print("\nEmployees with salary > ₹50,000:")
for emp_id, emp_info in employees.items():
    if emp_info["salary"] > 50000:
        print(f"  {emp_info['name']} (₹{emp_info['salary']})")
```
➡️ Filters and lists employees earning more than ₹50,000.

---

## 🔹 Employees Grouped by Location

```python
location_count = {}
for emp_info in employees.values():
    loc = emp_info["location"]
    location_count[loc] = location_count.get(loc, 0) + 1

print("\nEmployees count per location:")
for location, count in location_count.items():
    print(f"  {location}: {count}")
```
➡️ Groups employees by `location` and counts how many work in each city.

---

## 🔹 Average Salary Per Department

```python
dept_salary = {}
dept_count = {}

for emp_info in employees.values():
    dept = emp_info["department"]
    dept_salary[dept] = dept_salary.get(dept, 0) + emp_info["salary"]
    dept_count[dept] = dept_count.get(dept, 0) + 1

print("\nAverage salary per department:")
for dept in dept_salary:
    avg_salary = dept_salary[dept] / dept_count[dept]
    print(f"  {dept}: ₹{avg_salary:.2f}")
```
➡️ Calculates average salary for each department using sum/count approach.

---

## 🔹 List Employees in a Given Department

```python
search_dept = input("\nEnter department name to search: ")
print(f"\nEmployees in {search_dept} department:")
found = False
for emp_info in employees.values():
    if emp_info["department"].lower() == search_dept.lower():
        print(f"  {emp_info['name']}")
        found = True

if not found:
    print("  No employees found in this department.")
```
➡️ Searches employees by department input (case-insensitive).

---

## 🔹 Highest Paid Employee

```python
max_salary = -1
top_employee = None

for emp_id, emp_info in employees.items():
    if emp_info["salary"] > max_salary:
        max_salary = emp_info["salary"]
        top_employee = (emp_id, emp_info)

if top_employee:
    print(f"\nHighest Paid Employee:\n  ID: {top_employee[0]}")
    print(f"  Name: {top_employee[1]['name']}, Salary: ₹{top_employee[1]['salary']}")
```
➡️ Identifies and displays the employee with the highest salary.

---

## 🔹 Sort Employees by Salary (Descending)

```python
print("\nEmployees sorted by salary (high to low):")
sorted_emps = sorted(employees.items(), key=lambda item: item[1]['salary'], reverse=True)
for emp_id, emp_info in sorted_emps:
    print(f"  {emp_info['name']} - ₹{emp_info['salary']}")
```
➡️ Sorts the employees in descending order of their salary.

---

Let me know if you'd like this markdown saved as a `.md` file for download.
