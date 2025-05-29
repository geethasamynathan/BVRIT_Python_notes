
# 🔒 Closures in Python

## ✅ What is a Closure?

A **closure** is a function **object** that has access to variables in its **enclosing lexical scope**, even after the outer function has **finished executing**.

> **A closure is a nested function that remembers the values of variables from its enclosing function, even if the outer function is no longer in scope.**

---

## ✅ Components of a Closure

1. There must be a **nested function**.
2. The nested function must **refer to a value** defined in the enclosing function.
3. The enclosing function must **return the nested function**.

---

## 🧪 Example of a Closure

```python
def multiplier(factor):
    def multiply(number):
        return number * factor  # `factor` is retained from outer scope
    return multiply

# Creating a closure
double = multiplier(2)
triple = multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
```

Even though the `multiplier` function has finished executing, `double` and `triple` **remember** the value of `factor` — that's the **closure**.

---

## 📌 When to Use Closures

| Use Case | Description |
|----------|-------------|
| **Encapsulation** | Closures can hide variables from global scope (data hiding) |
| **Customizable Functions** | Generate functions with embedded configuration (like `double`, `triple`) |
| **Callbacks/Event Handlers** | Maintain context/state without using classes |
| **Decorators** | Python decorators use closures to extend functionality |

---

## 🔄 How It Differs from a Simple Nested Function

| Feature                   | Nested Function            | Closure                          |
|---------------------------|----------------------------|-----------------------------------|
| Returned to outer scope? | No                         | Yes                               |
| Remembers outer variables | No                         | Yes                               |
| Can be reused later       | Only within parent scope   | Anywhere                          |
| Example Use               | Helper methods             | Configurable functions, callbacks |

---

## 🔁 Nested Function Example (Without Closure)

```python
def greet():
    def say_hello():
        return "Hello"
    print(say_hello())  # Accessible only inside greet

greet()
# say_hello()  # ❌ Error: NameError
```

The `say_hello` function **cannot be used outside** `greet`.

---

## 🔁 Closure Example (Reused Outside)

```python
def make_greeter(name):
    def greet():
        return f"Hello, {name}"
    return greet

greeting = make_greeter("Gopi")
print(greeting())  # Hello, Gopi
```

Here, `greeting()` is a closure that **remembers** the value of `name = "Gopi"` even after `make_greeter()` is done.
