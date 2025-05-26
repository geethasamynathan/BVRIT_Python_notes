# 🎯 Python Control Statement Assignments with Solutions

---

## ✅ Assignment 1: ATM Machine Simulation

**Problem:** Simulate an ATM that allows checking balance, withdrawing, depositing, and exiting.

```python
balance = 5000
pin = "1234"

entered_pin = input("Enter your PIN: ")
if entered_pin == pin:
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Your balance is ₹{balance}")
        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("Deposited successfully.")
        elif choice == "3":
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawn successfully.")
            else:
                print("Insufficient funds.")
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid option.")
else:
    print("Incorrect PIN.")
```

---

## ✅ Assignment 2: Student Grade Calculator

**Problem:** Input 5 subject marks and assign a grade.

```python
marks = []
for i in range(5):
    marks.append(float(input(f"Enter mark {i+1}: ")))

avg = sum(marks) / 5

if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Average: {avg:.2f}, Grade: {grade}")
```

---

## ✅ Assignment 3: Traffic Light System

**Problem:** Input color and output traffic instruction.

```python
color = input("Enter traffic light color (red/yellow/green): ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color!")
```

---

## ✅ Assignment 4: Electricity Bill Generator

```python
units = int(input("Enter electricity units consumed: "))

if units <= 100:
    cost = units * 5
elif units <= 300:
    cost = units * 8
else:
    cost = units * 10

if cost > 2000:
    cost += cost * 0.18  # GST 18%

print(f"Total Bill: ₹{cost:.2f}")
```

---

## ✅ Assignment 5: Password Strength Checker

```python
password = input("Enter password: ")

has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)

if len(password) >= 8 and has_upper and has_digit:
    print("Strong Password")
else:
    print("Weak Password")
```

---

## ✅ Assignment 6: Shopping Cart Discount

```python
total = float(input("Enter total cart amount: "))

if total > 5000:
    discount = 0.2
elif total > 3000:
    discount = 0.1
else:
    discount = 0.0

final = total - (total * discount)
print(f"Final amount after discount: ₹{final:.2f}")
```

---

## ✅ Assignment 7: Odd/Even Counter

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Even: {even}, Odd: {odd}")
```

---

## ✅ Assignment 8: Login Attempts

```python
password = "secure123"
attempts = 0

while attempts < 3:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Login successful!")
        break
    else:
        print("Incorrect password.")
        attempts += 1

if attempts == 3:
    print("Account locked due to 3 failed attempts.")
```

---

## ✅ Assignment 9: Dice Roll Until 6 Appears

```python
import random

rolls = 0
while True:
    rolls += 1
    dice = random.randint(1, 6)
    print(f"Rolled: {dice}")
    if dice == 6:
        break

print(f"It took {rolls} rolls to get a 6.")
```

---

## ✅ Assignment 10: Number Guessing Game

```python
import random
target = random.randint(1, 100)

while True:
    guess = int(input("Guess the number (1-100): "))
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("Correct! You win!")
        break
```