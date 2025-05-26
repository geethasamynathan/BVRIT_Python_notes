
# 🐍 Python: Difference Between `@classmethod`, `@staticmethod`, and Normal Method

## 🔍 Difference Table

| Feature                    | Normal Method (`self`)            | Class Method (`@classmethod`)         | Static Method (`@staticmethod`)          |
|----------------------------|------------------------------------|---------------------------------------|------------------------------------------|
| Access to instance (`self`)| ✅ Yes                             | ❌ No                                 | ❌ No                                     |
| Access to class (`cls`)    | ❌ No                              | ✅ Yes                                | ❌ No                                     |
| Can modify instance state  | ✅ Yes                             | ❌ No                                 | ❌ No                                     |
| Can modify class state     | ❌ No                              | ✅ Yes                                | ❌ No                                     |
| Bound to                   | Object instance                   | Class                                 | Class                                     |
| Use Case                   | Access/modify object properties   | Factory methods, access/modify class variables | Utility/helper methods that don’t need access to instance or class |

---

## ✅ Real-World Use Cases

### 1️⃣ Normal Method (`self`)
Used when you need to access or modify **instance variables**.

#### Example: Banking – Withdraw money
```python
class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"{amount} withdrawn. New balance: {self.balance}"
        return "Insufficient funds"
```

**➡️ When to use:** Use `self` when you are working with the **current object**'s state.

---

### 2️⃣ Class Method (`@classmethod`)
Used when you need to access or modify **class-level data**. Often used as **factory methods**.

#### Example: Create account with default balance
```python
class BankAccount:
    bank_name = "Python Bank"

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    @classmethod
    def create_with_min_balance(cls, holder):
        return cls(holder, balance=1000)
```

**➡️ When to use:**  
- When creating alternative constructors.  
- When modifying/accessing **class-level variables** (e.g., global config, shared counters).

---

### 3️⃣ Static Method (`@staticmethod`)
Used when you need a utility function that **doesn’t access `self` or `cls`**.

#### Example: Validating PAN number format
```python
class BankAccount:
    @staticmethod
    def validate_pan(pan):
        import re
        return bool(re.match(r'[A-Z]{5}[0-9]{4}[A-Z]', pan))
```

**➡️ When to use:**  
- When logic is **related to the class**, but doesn’t access/modify object or class state.  
- For **utility/helper functions** (e.g., formatting, validations, calculations).

---

## 🚦 Summary: When to Use Which?

| You want to...                                     | Use                  |
|----------------------------------------------------|-----------------------|
| Work with instance-specific data or behavior       | Normal method (`self`) |
| Work with or modify class-level data               | `@classmethod` (`cls`) |
| Use a helper function that doesn’t need `self` or `cls` | `@staticmethod`        |
