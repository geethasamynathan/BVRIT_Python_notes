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

no_of_Employees = int(input("Enter the number of employees: "))


for i in range(no_of_Employees):
        emp_id = input("Enter employee ID: ")
        emp_name = input("Enter employee name: ")
        emp_salary = float(input("Enter employee salary: "))
        emp_location = input("Enter employee location: ")
        emp_department = input("Enter employee department: ")
        emp_gender = input(" Enter employee  gender")
        
        employees[emp_id] = {"name": emp_name, "salary": emp_salary,"location": emp_location, "department": emp_department,"gender": emp_gender}
        
print("\nEmployee Details:")
for emp_id, emp_info in employees.items():
        print(f"Employee ID: {emp_id}")
        print(f" \n Name: {emp_info['name']}\t Salary: {emp_info['salary']}\t Location: {emp_info['location']}\t Department: {emp_info['department']}\t Gender: {emp_info['gender']}  ")
        print()  # blank line
        
# find the Number of employees in each department
department_count = {}
for emp_info in employees.values():
        department = emp_info["department"]
        if department in department_count:
            department_count[department] += 1
        else:
            department_count[department] = 1
print("Number of employees in each department:")
    
for department, count in department_count.items():
        print(f"  {department}: {count} employee(s)") 

# Find the total number of male and female employees.
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


## 
location_count = {}
for emp_info in employees.values():
    loc = emp_info["location"]
    location_count[loc] = location_count.get(loc, 0) + 1

print("\nEmployees count per location:")
for location, count in location_count.items():
    print(f"  {location}: {count}")

# Calculate the average salary of employees in each department.
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

# List all employees in a given department (user input).
search_dept = input("\nEnter department name to search: ")
print(f"\nEmployees in {search_dept} department:")
found = False
for emp_info in employees.values():
    if emp_info["department"].lower() == search_dept.lower():
        print(f"  {emp_info['name']}")
        found = True

if not found:
    print("  No employees found in this department.")

# Show the employee with the highest salary.
max_salary = -1
top_employee = None

for emp_id, emp_info in employees.items():
    if emp_info["salary"] > max_salary:
        max_salary = emp_info["salary"]
        top_employee = (emp_id, emp_info)

if top_employee:
    print(f"\nHighest Paid Employee:\n  ID: {top_employee[0]}")
    print(f"  Name: {top_employee[1]['name']}, Salary: ₹{top_employee[1]['salary']}")

# Display employees sorted by salary in descending order.

print("\nEmployees sorted by salary (high to low):")
sorted_emps = sorted(employees.items(), key=lambda item: item[1]['salary'], reverse=True)
for emp_id, emp_info in sorted_emps:
    print(f"  {emp_info['name']} - ₹{emp_info['salary']}")
