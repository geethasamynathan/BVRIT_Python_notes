inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]
# ---------- Task 1: Total revenue ----------
total_revenue = 0
for item in inventory:
    _, _, price, sold, _ = item
    total_revenue += price * sold

print(f"TOTAL REVENUE: ${total_revenue:,.2f}\n")


# ---------- Task 2: Category-wise revenue ----------
categories = ["Fruit", "Vegetable", "Dairy", "Bakery"]
cat_revenue = {cat: 0 for cat in categories}

for item in inventory:
    _, cat, price, sold, _ = item
    cat_revenue[cat] += price * sold

print("REVENUE BY CATEGORY:")
for cat in categories:
    print(f"  {cat:<10}: ${cat_revenue[cat]:,.2f}")
print()  # blank line


# ---------- Task 3: Low-stock alert (<5 units left) ----------
LOW_STOCK_THRESHOLD = 5
low_stock_items = []

for item in inventory:
    name, _, _, _, left = item
    if left < LOW_STOCK_THRESHOLD:
        low_stock_items.append((name, left))

print("LOW-STOCK ITEMS (<5 units left):")
if low_stock_items:
    for name, left in low_stock_items:
        print(f"  {name:<10} → {left} unit(s) remaining")
else:
    print("  None")
print()


# ---------- Task 4: Best-selling item (by units sold) ----------
best_item = None
max_units_sold = -1

for item in inventory:
    name, _, _, sold, _ = item
    if sold > max_units_sold:
        max_units_sold = sold
        best_item = name

print(f"BEST-SELLING ITEM: {best_item} ({max_units_sold} units sold)\n")


# ---------- Task 5: Apply 10 % discount to Bakery items ----------
DISCOUNT_RATE = 0.10

print("PRICE LIST FOR TOMORROW (Bakery items discounted 10 %):")
for item in inventory:
    name, cat, price, *_ = item
    if cat == "Bakery":
        price *= (1 - DISCOUNT_RATE)
    print(f"  {name:<10}: ${price:.2f}")
