
# 🐍 Python Functions Tutorial: Basic to Advanced

## 🧠 What is a Function in Python?

A **function** is a reusable block of code that performs a specific task.

### 🔧 Basic Syntax:
```python
def function_name(parameters):
    # code block
    return value
```

---

## 🧩 Parameters vs Arguments

| Term        | Description                                                                 | Example                              |
|-------------|-----------------------------------------------------------------------------|--------------------------------------|
| **Parameter** | A variable in the function definition.                                       | `def greet(name):` – `name` is a parameter |
| **Argument**  | The actual value you pass to a function when calling it.                   | `greet("Alice")` – `"Alice"` is an argument |

---

## 🐣 1. Basic Function Example

### ✨ Use Case: Greeting a user
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```

---

## 🔁 2. Function with Default Parameters

### ✨ Use Case: Shipping cost calculator with default country
```python
def shipping_cost(weight, country="USA"):
    if country == "USA":
        return weight * 5
    else:
        return weight * 10

print(shipping_cost(2))             # Uses default "USA"
print(shipping_cost(2, "Canada"))   # Overrides default
```

---

## 🧮 3. Function with Multiple Parameters

### ✨ Use Case: Calculate total bill including tax
```python
def total_bill(amount, tax_rate):
    return amount + (amount * tax_rate / 100)

print(total_bill(100, 5))  # Output: 105.0
```

---

## 🌐 4. Return Multiple Values from a Function

### ✨ Use Case: Basic analytics of a dataset
```python
def analyze_data(data):
    avg = sum(data) / len(data)
    min_val = min(data)
    max_val = max(data)
    return avg, min_val, max_val

scores = [80, 90, 78, 92]
avg, min_score, max_score = analyze_data(scores)
print(f"Avg: {avg}, Min: {min_score}, Max: {max_score}")
```

---

## 🧲 5. Variable-Length Arguments

### ✨ Use Case: Dynamic Shopping Cart

#### Using *args (Non-keyword arguments)
```python
def total_price(*prices):
    return sum(prices)

print(total_price(10, 20, 30, 15))  # Output: 75
```

#### Using **kwargs (Keyword arguments)
```python
def order_summary(**items):
    for item, qty in items.items():
        print(f"{item}: {qty} pcs")

order_summary(apple=2, banana=5, mango=3)
```

---

## 🧰 6. Nested Functions

### ✨ Use Case: Order validation
```python
def place_order(total):
    def apply_discount(t):
        return t * 0.9 if t > 100 else t
    final_amount = apply_discount(total)
    return final_amount

print(place_order(120))  # Output: 108.0
```

---

## 🚀 7. Lambda Functions (Anonymous Functions)

### ✨ Use Case: Quick tax calculator
```python
tax = lambda amount: amount * 0.18
print(tax(1000))  # Output: 180.0
```

---

## 🧠 8. Real-World Example: Restaurant Billing System

```python
def calculate_bill(menu_items):
    subtotal = sum(menu_items.values())
    tax = subtotal * 0.05
    tip = subtotal * 0.1
    total = subtotal + tax + tip
    return subtotal, tax, tip, total

order = {"Pasta": 250, "Juice": 100, "Cake": 150}
bill = calculate_bill(order)
print(f"Subtotal: {bill[0]}, Tax: {bill[1]}, Tip: {bill[2]}, Total: {bill[3]}")
```

---

## 🧪 9. Function as a Parameter

### ✨ Use Case: Apply a discount strategy
```python
def discount_price(price, strategy):
    return strategy(price)

def half_price(p):
    return p / 2

print(discount_price(200, half_price))  # Output: 100.0
```

---

## 🧵 10. Recursion

### ✨ Use Case: Factorial calculation
```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

---

## 📊 Summary Table

| Concept                     | Key Syntax                         | Use Case                                  |
|----------------------------|-------------------------------------|-------------------------------------------|
| Basic Function             | `def name():`                       | Greeting message                          |
| Default Parameter          | `def name(x=10):`                   | Default country in shipping               |
| Multiple Return            | `return a, b`                       | Min/Max/Average                           |
| *args                      | `def name(*args):`                  | Unlimited prices in cart                  |
| **kwargs                   | `def name(**kwargs):`               | Keyword items in order                    |
| Nested Function            | `def outer(): def inner():`         | Validation inside order function          |
| Lambda                     | `lambda x: x * 2`                   | Quick operations like tax                 |
| Function as Argument       | `def outer(fn):`                    | Strategy pattern                          |
| Recursion                  | `def f(n): return f(n-1)`           | Factorial, Tree traversal, etc.           |


## Scope of the variable

## 📘 What is Scope in Python?

Scope refers to **the region of the code where a variable is accessible**.

| Scope Type | Description |
|------------|-------------|
| **Local**  | Variable declared **inside** a function – accessible only within that function |
| **Global** | Variable declared **outside** all functions – accessible throughout the script |

---

## ✅ Example: Local and Global Scope

```python
x = 10  # Global variable

def show_scope():
    x = 5  # Local variable (shadows global x)
    print("Inside function (local x):", x)

show_scope()
print("Outside function (global x):", x)
```

### 🔍 Output:
```
Inside function (local x): 5
Outside function (global x): 10
```

---

## 🧠 Modifying Global Variable from Inside Function

To modify a global variable inside a function, use the `global` keyword:

```python
count = 0

def increment():
    global count
    count += 1
    print("Inside function:", count)

increment()
print("Outside function:", count)
```

### 🔍 Output:
```
Inside function: 1
Outside function: 1
```

---

## ⚠️ Notes:

- Local variables exist only inside the function where they are defined.
- Global variables can be accessed from anywhere, but to **modify** them inside a function, you must use the `global` keyword.
- Local variables **override** global variables with the same name inside functions.
- Prefer **returning values** from functions instead of modifying global variables for better readability and maintainability.

---
