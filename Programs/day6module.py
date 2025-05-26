# import os
# print("Current Directory:", os.getcwd())
# print("Files:", os.listdir('.'))

# import json
# data = {"name": "Geetha", "age": 25}
# json_str = json.dumps(data)
# print("JSON:", json_str)


class Employee:
    @classmethod
    def display(cls):
        return "Employee class method called"
    
    def sample(self):
        return "Sample method called"
    
# print(Employee.display())
employee= Employee()
print(employee.display())  # This will raise an error because display is a static method    
print(type(employee.display))  # This will print the type of the employee object
print(employee.sample())  # This will call the sample method of the Employee class