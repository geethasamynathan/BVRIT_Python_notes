
# 🧪 Python Function Exercises – Real World Scenarios

---

## 1. Temperature Converter

### Problem:
Convert Celsius to Fahrenheit.

### Solution:
```python
def convert_temperature(celsius):
    return (celsius * 9/5) + 32

print(convert_temperature(0))    # 32.0
print(convert_temperature(100))  # 212.0
```

---

## 2. Bill Splitter

### Problem:
Split a bill equally among people.

### Solution:
```python
def split_bill(total, num_people):
    return round(total / num_people, 2)

print(split_bill(1000, 4))  # 250.0
```

---

## 3. Email Formatter

### Problem:
Generate email from user’s full name.

### Solution:
```python
def format_email(name):
    parts = name.strip().lower().split()
    return f"{parts[0]}.{parts[1]}@gmail.com"

print(format_email("John Doe"))  # john.doe@gmail.com
```

---

## 4. Shopping Cart Total with Discount

### Problem:
Calculate final price after discount.

### Solution:
```python
def calculate_total(cart, discount):
    subtotal = sum(cart.values())
    final_price = subtotal - (subtotal * discount / 100)
    return round(final_price, 2)

items = {"Shoes": 1200, "Hat": 300, "Bag": 1500}
print(calculate_total(items, 10))  # 2700.0
```

---

## 5. Determine Leap Year

### Problem:
Check if a year is a leap year.

### Solution:
```python
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap_year(2024))  # True
print(is_leap_year(1900))  # False
```

---

## 6. Grade Calculator

### Problem:
Assign grades based on score.

### Solution:
```python
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(get_grade(85))  # B
```

---

## 7. ATM Withdrawal Validation

### Problem:
Allow withdrawal if amount is ≤ balance and multiple of 100.

### Solution:
```python
def can_withdraw(balance, amount):
    return amount <= balance and amount % 100 == 0

print(can_withdraw(1500, 300))  # True
print(can_withdraw(1500, 250))  # False
```

---

## 8. Employee Bonus Calculator

### Problem:
Calculate bonus based on performance rating.

### Solution:
```python
def calculate_bonus(salary, rating):
    if rating == 5:
        return salary * 0.2
    elif rating == 4:
        return salary * 0.1
    else:
        return 0

print(calculate_bonus(50000, 5))  # 10000
```

---

## 9. String Word Counter

### Problem:
Count the number of words in a sentence.

### Solution:
```python
def count_words(text):
    return len(text.strip().split())

print(count_words("Python is easy to learn"))  # 5
```

---

## 10. Flight Ticket Calculator with Optional Meal

### Problem:
Calculate total cost based on meal inclusion.

### Solution:
```python
def flight_price(base_price, has_meal=False):
    return base_price + 500 if has_meal else base_price

print(flight_price(3500, True))  # 4000
```

---
