
# 🎯 Python Function Decorators – Basic to Advanced

## 🧠 What is a Function Decorator?

A **function decorator** is a special function in Python used to **modify or enhance the behavior of another function without changing its actual code**.

---

## 🎯 When to Use a Decorator?

Use a decorator when:
- You want to **add common logic** (like logging, timing, authentication) to many functions.
- You need to **reuse** logic **before and/or after** a function call.
- You want **cleaner and more modular code**.

---

## ⚖️ Decorator vs Normal Function

| Feature                     | Normal Function                        | Decorator Function                              |
|-----------------------------|----------------------------------------|--------------------------------------------------|
| Purpose                     | Performs a specific task               | Enhances or wraps another function               |
| Reusability                 | Used directly                          | Applied to other functions using `@decorator`    |
| Can modify other functions | ❌ No                                   | ✅ Yes                                            |
| Syntax                     | Called with parentheses `()`           | Used with `@decorator_name` before function def  |

---

## 🪜 Basic to Advanced Decorator in Python

### ✅ 1. Basic Decorator – Logging Example

```python
# Step 1: Define a decorator function
def my_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()  # original function is called
        print("After calling the function")
    return wrapper

# Step 2: Apply the decorator using @
@my_decorator
def greet():
    print("Hello, world!")

# Step 3: Call the function
greet()
```

### 🔍 Line-by-line Explanation

| Line | Explanation |
|------|-------------|
| `def my_decorator(func):` | The decorator takes a function as an argument. |
| `def wrapper():` | This is the wrapper that adds extra logic. |
| `print("Before...")` | Runs **before** the original function. |
| `func()` | Calls the **original function** (`greet()` here). |
| `print("After...")` | Runs **after** the original function. |
| `return wrapper` | Returns the wrapped function. |
| `@my_decorator` | Applies the decorator to `greet()`. |
| `greet()` | Actually runs `wrapper()`, not `greet()` directly. |

---

### ✅ 2. Decorator with Arguments

```python
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function
def add(x, y):
    return x + y

print(add(3, 5))
```

### 🔍 Explanation

- `*args` and `**kwargs` let you accept any number of arguments.
- `func.__name__` gets the original function name (`add`).

Output:
```
Calling add with args=(3, 5), kwargs={}
8
```

---

### ✅ 3. Real-World Example – Access Control

```python
def require_admin(func):
    def wrapper(user):
        if user != "admin":
            print("Access Denied!")
            return
        return func(user)
    return wrapper

@require_admin
def view_dashboard(user):
    print(f"Welcome, {user}. Here is your dashboard.")

view_dashboard("guest")   # Access Denied!
view_dashboard("admin")   # Welcome, admin...
```

---

## 💡 Advanced: Decorators with Parameters

```python
def repeat(n):  # outermost function takes parameter
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
```

---

## 🔚 Summary: Why Use Decorators?

| Use Case         | Benefit                          |
|------------------|----------------------------------|
| Logging          | Monitor function calls           |
| Validation       | Check permissions/authentication |
| Reusability      | Avoid duplicate code             |
| Code Cleanliness | Separation of concern            |


# Assignment
## Problem Statement:
In an admin dashboard, every time a user accesses a sensitive function (like viewing user data or transferring money), you want to log the access time and username, without rewriting the logging logic in every function.

✅ Solution: Use a Function Decorator
```python
import datetime

# Decorator function for logging
def log_access(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get('user', 'Unknown')
        print(f"[{datetime.datetime.now()}] Accessed by: {user} | Function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Example of a sensitive operation
@log_access
def view_account_details(account_id, user=None):
    print(f"Showing account details for Account ID: {account_id}")

@log_access
def transfer_funds(from_acc, to_acc, amount, user=None):
    print(f"Transferring ₹{amount} from {from_acc} to {to_acc}")

# Simulate users accessing the functions
view_account_details(1001, user='admin_user')
transfer_funds(1001, 1002, 5000, user='finance_manager')

```

🔍 Output:
```yaml
[2025-05-25 10:30:45.123456] Accessed by: admin_user | Function: view_account_details
Showing account details for Account ID: 1001

[2025-05-25 10:30:45.123789] Accessed by: finance_manager | Function: transfer_funds
Transferring ₹5000 from 1001 to 1002
```
| Aspect              | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| **Problem Solved**  | Avoid repeating logging logic in multiple secure functions                  |
| **Decorator Role**  | Wraps any function to add reusable pre/post-processing logic (here, logging)|
| **Real-world Relevance** | Used in admin portals, finance systems, API access logs           