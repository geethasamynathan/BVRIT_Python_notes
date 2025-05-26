class Employee:
    employee_count = 0
    id_counter = 1001  # Unique ID starting point

    def __init__(self, name, age, position):
        self.emp_id = Employee.id_counter
        self.name = name
        self.age = age
        self.position = position
        Employee.employee_count += 1
        Employee.id_counter += 1

    def display_employee_info(self):
        print("Employee Information:")
        print("-----------------------")
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Position: {self.position}")

    @classmethod
    def get_total_employees(cls):
        return cls.employee_count


# Store employees in a dictionary {emp_id: Employee}
employees = {}

# 1. Get number of employees to add
num = int(input("How many employees do you want to add? "))

# 2. Take input and create employee objects
for _ in range(num):
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    position = input("Enter employee position: ")

    emp = Employee(name, age, position)
    employees[emp.emp_id] = emp
    print(f"Employee {emp.emp_id} added successfully!\n")

# 3. Show total employees
print(f"\nTotal Employees Added: {Employee.get_total_employees()}")

# 4. Search Functions
def search_by_id(emp_id):
    if emp_id in employees:
        employees[emp_id].display_employee_info()
    else:
        print(f"No employee found with ID {emp_id}")

def search_by_name_contains(partial_name):
    found = False
    for emp in employees.values():
        if partial_name.lower() in emp.name.lower():
            emp.display_employee_info()
            found = True
    if not found:
        print("No matching employee found.")

def search_by_name_startswith(prefix):
    found = False
    for emp in employees.values():
        if emp.name.lower().startswith(prefix.lower()):
            emp.display_employee_info()
            found = True
    if not found:
        print("No matching employee found.")

# 5. Menu for search
while True:
    print("\n--- Search Menu ---")
    print("1. Search by ID")
    print("2. Search by Name (contains)")
    print("3. Search by Name (starts with)")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            search_id = int(input("Enter Employee ID to search: "))
            search_by_id(search_id)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "2":
        name_part = input("Enter part of the name to search: ")
        search_by_name_contains(name_part)
    elif choice == "3":
        name_prefix = input("Enter name prefix to search: ")
        search_by_name_startswith(name_prefix)
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please select again.")
