
# ✅ Python Unit Testing Tutorial (Basic to Advanced)

## 📌 What is `unittest` in Python?

`unittest` is Python’s built-in module for unit testing. It helps you test your code for correctness, catch bugs early, and maintain code quality.

It supports:
- Test discovery
- Fixtures (`setUp`, `tearDown`)
- Assertions
- Test suites and mocking

> ✅ No need to install — part of the Python standard library.

---

## 🛠️ How to Run Unit Tests

### Run a single test file:
```bash
python -m unittest test_file.py
```

### Run all test files in a directory:
```bash
python -m unittest discover
```

### Run inside a Python script:
```python
unittest.main()
```

---

## 🗂️ Recommended Folder Structure

```
project/
│
├── app/
│   ├── calculator.py
│
└── tests/
    ├── test_calculator.py
```

---

## 📘 Basic Example

### `app/calculator.py`

```python
def add(x, y):
    return x + y

def divide(x, y):
    return x / y
```

### `tests/test_calculator.py`

```python
import unittest
from app.calculator import add, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

---

## 🧪 Common `unittest` Assertions

| Assertion | Description |
|-----------|-------------|
| `assertEqual(a, b)` | Check a == b |
| `assertNotEqual(a, b)` | Check a != b |
| `assertTrue(x)` | Check bool(x) is True |
| `assertFalse(x)` | Check bool(x) is False |
| `assertIs(a, b)` | a is b |
| `assertIsNone(x)` | x is None |
| `assertIn(a, b)` | a in b |
| `assertRaises(Exception)` | Check that an exception is raised |

---

## ⚙️ Setup and Teardown

```python
class TestExample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Run once before all tests")

    def setUp(self):
        print("Run before each test")

    def tearDown(self):
        print("Run after each test")

    @classmethod
    def tearDownClass(cls):
        print("Run once after all tests")
```

---

## 🧠 Real-World Cart Example

### `cart.py`

```python
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.items.append((name, quantity))

    def total_items(self):
        return sum(q for _, q in self.items)
```

### `test_cart.py`

```python
import unittest
from cart import Cart

class TestCart(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()

    def test_add_item(self):
        self.cart.add_item("Apple", 2)
        self.assertEqual(self.cart.total_items(), 2)

    def test_add_zero_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("Banana", 0)

if __name__ == '__main__':
    unittest.main()
```

---

## 🧩 Mocking with `unittest.mock`

```python
from unittest.mock import patch
import requests
import unittest

def get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    return response.json()

class TestAPI(unittest.TestCase):

    @patch('requests.get')
    def test_get_user(self, mock_get):
        mock_get.return_value.json.return_value = {"name": "John"}
        user = get_user()
        self.assertEqual(user["name"], "John")
```

---

## ⚡ Advanced CLI Options

### Run all tests recursively:
```bash
python -m unittest discover -s tests -p "test_*.py"
```

### Verbose output:
```bash
python -m unittest discover -v
```

---

## ✅ Best Practices

- Name test files as `test_*.py`
- Keep test functions small and isolated
- Use mocking for external dependencies
- Integrate with CI tools (GitHub Actions, Jenkins, etc.)
- Group logically related tests in classes

---

## 🔚 Conclusion

`unittest` is powerful, flexible, and supports both small and large projects. Mastering it ensures code reliability and confidence in changes or refactoring.
