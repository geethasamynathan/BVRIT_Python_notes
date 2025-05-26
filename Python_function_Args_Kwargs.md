
# 🔹 Python Functions with `*args` and `**kwargs`

In Python, `*args` and `**kwargs` are used in function definitions to allow **variable numbers of arguments** to be passed.

---

## ✅ `*args`: Variable-length positional arguments

- Collects **extra positional arguments** as a tuple.
```python
def func(*args):
    print(args)

func(1, 2, 3)  # Output: (1, 2, 3)
```

---

## ✅ `**kwargs`: Variable-length keyword arguments

- Collects **extra keyword arguments** as a dictionary.
```python
def func(**kwargs):
    print(kwargs)

func(a=1, b=2)  # Output: {'a': 1, 'b': 2}
```

---

## 🧠 When to Use

| Scenario | Use `*args` | Use `**kwargs` |
|----------|-------------|----------------|
| You don’t know how many positional arguments will be passed | ✅ Yes | ❌ No |
| You don’t know how many named keyword arguments will be passed | ❌ No | ✅ Yes |
| Flexible APIs or wrappers | ✅ Yes | ✅ Yes |
| Dynamic configuration or settings | ❌ No | ✅ Yes |

---

## 📌 Real-World Examples

### 1. Billing Function with Dynamic Item Prices (`*args`)
```python
def calculate_total(*prices):
    return sum(prices)

total = calculate_total(100, 250, 399)
print(total)  # 749
```

---

### 2. Creating a User Profile with Flexible Data (`**kwargs`)
```python
def create_user_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

create_user_profile(name="Alice", age=30, email="alice@example.com")
```

### Output:
```
Name: Alice
Age: 30
Email: alice@example.com
```

---

### 3. Combining Both `*args` and `**kwargs`
```python
def handle_order(order_id, *items, **customer_info):
    print(f"Order ID: {order_id}")
    print("Items:", items)
    print("Customer Info:", customer_info)

handle_order(101, "Shampoo", "Soap", name="John", city="Mumbai")
```

---

## 🔁 Function Signature Order Rule

Always use in this order:
```python
def func(required, *args, default=None, **kwargs):
    pass
```

---
