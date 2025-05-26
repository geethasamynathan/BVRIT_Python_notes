
# 👩‍💻 Python Example: Instance Method vs Class Method vs Static Method in a Class

## ✅ Base Class: `Employee` with Instance Method

```python
class Employee:
    def __init__(self):
        self.name = "Tina"
        self.age = 30
        self.position = "Software Engineer"

    def display_employee_info(self):  # Instance method
        print("Employee Information:")
        print("-----------------------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Position: {self.position}")
```

### ✅ Why Use Instance Method?

- Accesses **individual object data** like `self.name`, `self.age`, etc.
- Use when behavior is **specific to each instance** of the class.

---

## 📘 Class Method – Working with Class-Level Data or Factory Methods

```python
class Employee:
    employee_count = 0  # Class variable

    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        Employee.employee_count += 1

    @classmethod
    def from_string(cls, emp_str):
        name, age, position = emp_str.split(",")
        return cls(name, int(age), position)

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count
```

### 🟣 Why Use Class Method?

- Works with **class-level variables** like `employee_count`
- Good for **alternative constructors** (`from_string`), where you return a new object in a different way

---

## 🛠️ Static Method – For Independent Utility Logic

```python
    @staticmethod
    def is_valid_age(age):
        return 18 <= age <= 65
```

### 🔵 Why Use Static Method?

- Doesn’t use `self` or `cls`
- Ideal for **helper functions** that logically belong to the class but don't interact with it directly

---

## ✅ Complete Code with All Three Types

```python
class Employee:
    employee_count = 0

    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        Employee.employee_count += 1

    def display_employee_info(self):  # Instance Method
        print("Employee Information:")
        print("-----------------------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Position: {self.position}")

    @classmethod
    def from_string(cls, emp_str):  # Class Method
        name, age, position = emp_str.split(",")
        return cls(name, int(age), position)

    @classmethod
    def get_employee_count(cls):  # Class Method
        return cls.employee_count

    @staticmethod
    def is_valid_age(age):  # Static Method
        return 18 <= age <= 65


# Usage:
emp1 = Employee("Tina", 30, "Software Engineer")
emp2 = Employee.from_string("Tom,35,Manager")

emp1.display_employee_info()
print(f"Total Employees: {Employee.get_employee_count()}")

print("Is 45 a valid age?", Employee.is_valid_age(45))
print("Is 16 a valid age?", Employee.is_valid_age(16))
```

---

## 🔚 Summary Table

| Method Type     | Purpose                              | Example                             |
|------------------|---------------------------------------|-------------------------------------|
| Instance Method  | Access or modify object data          | `display_employee_info()`           |
| Class Method     | Access or modify class-level data     | `get_employee_count()`, `from_string()` |
| Static Method    | Utility method related to the class   | `is_valid_age(age)`                 |
