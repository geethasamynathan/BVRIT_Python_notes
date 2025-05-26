
# 🧨 Python Exception Handling Tutorial

## 📘 What is an Exception?

An **exception** is an error that occurs during the execution of a program. Instead of crashing the program, we can **handle** these exceptions using Python’s `try-except` block.

---

## 🧱 Basic Syntax

```python
try:
    # risky code
except SomeException:
    # handling code
```

---

## ✅ Real-World Example: Divide by Zero

```python
def divide(x, y):
    try:
        result = x / y
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

divide(10, 2)  # Result: 5.0
divide(10, 0)  # Error: Cannot divide by zero!
```

---

## 🧱 Catching Multiple Exceptions

### ✅ Use Case: File operations and type conversion

```python
try:
    number = int("xyz")
    with open("data.txt") as f:
        content = f.read()
except ValueError:
    print("Invalid number format.")
except FileNotFoundError:
    print("File not found.")
```

---

## 🧠 Using `else` Block

The `else` block runs **only if no exception is raised**.

```python
try:
    value = int("123")
except ValueError:
    print("Conversion failed.")
else:
    print("Conversion successful:", value)
```

---

## 🧹 Using `finally` Block

The `finally` block **always runs**, whether an exception occurs or not.

```python
try:
    f = open("example.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File missing.")
finally:
    print("Closing file or cleaning up resources.")
```

---

## 🛠 Raising Custom Exceptions

You can raise your own exceptions using `raise`.

```python
def withdraw(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    return f"Withdrawing {amount}"

try:
    print(withdraw(-500))
except ValueError as e:
    print("Caught exception:", e)
```

---

## 💼 Real-World Example: ATM Withdrawal System

```python
def atm_withdraw(balance, amount):
    try:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if amount > balance:
            raise ValueError("Insufficient balance.")
        print(f"Dispensed: ₹{amount}")
    except ValueError as e:
        print("Transaction failed:", e)
    finally:
        print("Thank you for using our ATM.")

atm_withdraw(1000, 1500)  # Insufficient balance
atm_withdraw(1000, 500)   # Success
```

---

## 🧠 Summary Table

| Keyword     | Purpose                                | Runs When                    |
|-------------|----------------------------------------|------------------------------|
| `try`       | Code block to test for errors          | Always                       |
| `except`    | Handle specific error                  | If matching exception raised |
| `else`      | Run if no exception                    | Only if no error             |
| `finally`   | Always run for cleanup                 | Always                       |
| `raise`     | Manually trigger exception             | Based on custom condition    |
