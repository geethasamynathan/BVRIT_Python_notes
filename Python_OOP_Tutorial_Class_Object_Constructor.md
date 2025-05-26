
# 🧠 Python OOP Tutorial: Class, Object, Access Specifiers & Constructor

---

## 📘 What is a Class?

A **class** is a blueprint for creating objects. It defines variables (attributes) and functions (methods) that describe behaviors of the object.

---

## 📦 What is an Object?

An **object** is an instance of a class. It contains real values for the attributes defined in the class and can use its methods.

---

## 🧱 Class Structure

```python
class ClassName:
    def __init__(self, args):  # Constructor
        self.attribute = value

    def method_name(self):
        pass
```

---

## 🔐 Access Specifiers in Python

Python uses naming conventions for access control:

| Type       | Syntax          | Meaning                                  |
|------------|------------------|------------------------------------------|
| Public     | `self.name`      | Accessible everywhere                    |
| Protected  | `self._name`     | Meant to be accessed in subclasses only  |
| Private    | `self.__name`    | Accessible only within the class         |

---

## 💼 Real-World Example: Bank Account System

```python
class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance):
        # Public variable
        self.account_number = account_number
        self.holder_name = holder_name

        # Protected variable
        self._balance = initial_balance

        # Private variable
        self.__pin = "1234"  # Default pin

    # Public method
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self._balance}")
        else:
            print("Invalid deposit amount")

    # Protected method
    def _calculate_interest(self):
        interest = self._balance * 0.04
        return interest

    # Private method
    def __validate_pin(self, pin):
        return pin == self.__pin

    # Public method that uses private method
    def withdraw(self, amount, pin):
        if self.__validate_pin(pin):
            if 0 < amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew ₹{amount}. Remaining balance: ₹{self._balance}")
            else:
                print("Insufficient balance or invalid amount")
        else:
            print("Invalid PIN!")

    def show_details(self):
        print(f"Account Holder: {self.holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self._balance}")
```

---

## 🧪 Using the Class

```python
# Creating object
acc1 = BankAccount("SB1001", "Alice", 5000)

# Deposit
acc1.deposit(2000)

# Access protected attribute (not recommended)
print("Accessing balance:", acc1._balance)

# Access private variable (will fail)
# print(acc1.__pin)  # ❌ AttributeError

# Access private variable via name mangling (not recommended)
print("Accessing private pin:", acc1._BankAccount__pin)

# Withdraw with wrong PIN
acc1.withdraw(1000, "0000")

# Withdraw with correct PIN
acc1.withdraw(1000, "1234")

# Display account details
acc1.show_details()
```

---

## 🖨️ Sample Output

```
Deposited ₹2000. New balance: ₹7000
Accessing balance: 7000
Accessing private pin: 1234
Invalid PIN!
Withdrew ₹1000. Remaining balance: ₹6000
Account Holder: Alice
Account Number: SB1001
Balance: ₹6000
```

---

## ✅ Summary Table

| Feature            | Syntax            | Access Scope                     |
|--------------------|-------------------|----------------------------------|
| Public Attribute   | `self.name`       | Anywhere                         |
| Protected Attribute| `self._name`      | Class & subclass (convention)    |
| Private Attribute  | `self.__name`     | Within the class (name mangling)|
| Constructor        | `__init__()`      | Initializes object during creation |
| Method             | `def method()`    | Defines behavior of object       |
