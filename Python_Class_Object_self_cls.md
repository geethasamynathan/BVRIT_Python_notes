
# 🧱 Python Class and Object – With `self` and `cls` Explained

## 🔷 What are Class and Object?

- A **class** is a blueprint for creating objects.
- An **object** is an instance of a class that contains real values.

---

## 🔹 Difference Between `self` and `cls`

| Keyword | Refers To | Used In           | Purpose                                      |
|---------|-----------|------------------|----------------------------------------------|
| `self`  | Instance  | Instance methods | Access instance variables and methods        |
| `cls`   | Class     | Class methods    | Access class-level variables and methods     |

---

## 📦 Real-world Example: Online Shopping Cart

### ✅ Python Code

```python
class ShoppingCart:
    total_carts = 0  # Class variable (shared across all instances)

    def __init__(self, user):
        self.user = user            # Instance variable
        self.items = []             # Instance variable
        ShoppingCart.total_carts += 1

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} added to {self.user}'s cart.")

    def view_cart(self):
        print(f"{self.user}'s cart contains: {', '.join(self.items)}")

    @classmethod
    def total_cart_count(cls):
        print(f"Total carts created: {cls.total_carts}")
```

---

### 💡 Explanation

- `self.user`, `self.items`: These are **instance variables**, specific to each object.
- `ShoppingCart.total_carts`: A **class variable**, shared among all instances.
- `add_item`, `view_cart`: Use `self` to access instance-specific data.
- `total_cart_count`: Uses `cls` to access class-level data (like total carts).

---

### 🎯 Usage

```python
# Create carts (objects)
cart1 = ShoppingCart("Alice")
cart2 = ShoppingCart("Bob")

cart1.add_item("Laptop")
cart2.add_item("Smartphone")
cart1.view_cart()
cart2.view_cart()

# Call class method
ShoppingCart.total_cart_count()
```

---

## 📘 When to Use `self` and `cls`

| Situation                                      | Use  |
|------------------------------------------------|------|
| Accessing or modifying instance variables      | `self` |
| Accessing or modifying class-wide variables    | `cls` |
| Defining methods that don't depend on instance or class | Use `@staticmethod` (no `self` or `cls`) |

---
