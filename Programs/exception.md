# 🧾 Real-World Example: Handling Different Exceptions in Python

## ✅ Scenario: Bank Withdrawal System

You're creating a simple bank withdrawal system where a user enters an amount to withdraw. You’ll handle different types of possible errors:

- `ValueError`: if the input is not a number.
- `ZeroDivisionError`: to simulate a possible division error (e.g., charge calculation).
- `FileNotFoundError`: if the log file is missing.
- General `Exception`: fallback for any unexpected error.

---

## ✅ Python Code Example

```python
def withdraw_funds(balance):
    try:
        amount = float(input("Enter the amount to withdraw: "))
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        
        if amount > balance:
            raise Exception("Insufficient balance.")

        # Simulate a charge calculation that might cause ZeroDivisionError
        charges = amount / 0  # This will raise ZeroDivisionError

        balance -= amount
        print(f"Withdrawal successful. Remaining balance: ₹{balance:.2f}")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    
    except ZeroDivisionError:
        print("Error: Division by zero occurred while calculating charges.")
    
    except FileNotFoundError:
        print("Log file not found. Cannot log transaction.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    else:
        print("Transaction processed without any error.")
    
    finally:
        print("Thank you for using our banking system.\n")

# Simulate user interaction
current_balance = 1000.0
withdraw_funds(current_balance)

```
