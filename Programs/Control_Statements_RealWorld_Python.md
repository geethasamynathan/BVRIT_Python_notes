# 🎢 Real-world Python Examples for Control Statements

## 🎯 Scenario: Theme Park Ticketing System

Determine ticket pricing and offers based on:
- Age
- VIP status
- Day type (weekday/weekend)
- Group size

---

## ✅ 1. if Statement

```python
age = 17

if age >= 18:
    print("You are eligible for adult ride access.")
```

---

## ✅ 2. if-else Statement

```python
is_vip = True

if is_vip:
    print("You get a VIP lounge pass!")
else:
    print("Upgrade to VIP for exclusive benefits.")
```

---

## ✅ 3. if-elif-else Statement

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It's a weekend! Prices are 20% higher.")
elif day == "Friday":
    print("Friday Special! 10% off for all visitors.")
else:
    print("Weekday normal pricing.")
```

---

## ✅ 4. Nested if Statement

```python
age = 12
is_vip = False

if age >= 10:
    if is_vip:
        print("You get 50% off as a VIP child.")
    else:
        print("Child ticket: $10")
```

---

## ✅ 5. for Loop

```python
group_ages = [10, 14, 32, 7, 18]

for person_age in group_ages:
    if person_age < 12:
        print("Child Ticket - $10")
    elif 12 <= person_age < 18:
        print("Teen Ticket - $15")
    else:
        print("Adult Ticket - $20")
```

---

## ✅ 6. while Loop

```python
countdown = 5

while countdown > 0:
    print(f"Ride starts in {countdown} seconds...")
    countdown -= 1
```

---

## ✅ 7. Simulated do-while Loop in Python

```python
total_guests = 0

while True:
    guest = input("Enter guest name (or 'done' to stop): ")
    if guest.lower() == "done":
        break
    total_guests += 1

print(f"Total guests entered: {total_guests}")
```

🔁 **Explanation**: The loop runs at least once, like a `do-while`.

---

## 🧠 Summary of Control Statements

| Control Statement | Purpose |
|-------------------|---------|
| `if`              | Check one condition |
| `if-else`         | Choose between two options |
| `if-elif-else`    | Choose among multiple conditions |
| `nested if`       | Decision within a decision |
| `for` loop        | Iterate over a known set (like a list) |
| `while` loop      | Repeat until a condition fails |
| `do-while` loop   | Repeat at least once (simulated with `while True`) |