
# 🛒 Extended Python Inventory Management Example

This example builds on a real-world **grocery store inventory** use case. It includes operations like adding, removing, sorting, and restocking items using various list methods and a dictionary for quantity management.

---

## ✅ Full Example Code

```python
# Initial inventory list
inventory = ["Apples", "Bananas", "Carrots"]
inventory.append("Dates")              # Add new item
inventory.remove("Bananas")            # Remove an item by value

# Check for availability
if "Carrots" in inventory:
    print("Carrots are in stock.")

# Sort items alphabetically
inventory.sort()
print("Sorted Inventory:", inventory)

# Add more items
inventory.extend(["Eggs", "Figs", "Grapes"])

# Remove item by index using del
del inventory[0]  # Removes 'Apples' after sorting

# Remove last item using pop
last_removed = inventory.pop()
print("Removed last item:", last_removed)

# Insert item at a specific position
inventory.insert(2, "Honey")

# Create a dictionary for quantities
stock_quantity = {
    "Carrots": 10,
    "Dates": 5,
    "Eggs": 12,
    "Figs": 0,
    "Grapes": 8,
    "Honey": 15
}

# Display available stock only
print("\nAvailable Stock:")
for item in inventory:
    quantity = stock_quantity.get(item, 0)
    if quantity > 0:
        print(f"{item}: {quantity} units")

# Restock Figs
stock_quantity["Figs"] = 20
print(f"\nFigs restocked: {stock_quantity['Figs']} units")

# Final inventory snapshot
print("\nFinal Inventory List:", inventory)
print("Final Stock Quantities:", stock_quantity)
```

---

## 💡 Sample Output

```
Carrots are in stock.
Sorted Inventory: ['Apples', 'Carrots', 'Dates']
Removed last item: Grapes

Available Stock:
Carrots: 10 units
Dates: 5 units
Eggs: 12 units
Honey: 15 units

Figs restocked: 20 units

Final Inventory List: ['Carrots', 'Dates', 'Honey', 'Eggs', 'Figs']
Final Stock Quantities: {'Carrots': 10, 'Dates': 5, 'Eggs': 12, 'Figs': 20, 'Grapes': 8, 'Honey': 15}
```

---

## 📌 Features Demonstrated

| Feature       | Purpose                                 |
|---------------|------------------------------------------|
| `append()`    | Add a single new item to the list        |
| `remove()`    | Remove by value                          |
| `del`         | Remove by index                          |
| `pop()`       | Remove and return last item              |
| `insert()`    | Insert item at a specific index          |
| `extend()`    | Add multiple items at once               |
| `in`          | Check for existence of an item           |
| `dict`        | Maintain quantity of each inventory item |
| `for` loop    | Display available items and filter stock |

---

## ✅ Real-World Application

- **Retail Software**: Manage store products and quantities.
- **Warehouse Systems**: Track goods using `dict` for quantity.
- **Point of Sale**: Dynamically adjust stock after purchase.

