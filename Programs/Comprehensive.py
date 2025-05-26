users = [("Alice", True), ("Bob", False), ("Charlie", True)]

active_users = [user for user in users if user[1]]
print(f"Active users: {active_users}")

active_users1=[name for name,status in users if status]
print(f"Active users: {active_users1}")
# This code snippet filters a list of users based on their active status and prints the active users.

product_codes = ["abc123", "xyz987", "def456"]
upper_codes = tuple(code.upper() for code in product_codes)
print(upper_codes)  # ('ABC123', 'XYZ987', 'DEF456')
print(type(upper_codes))  # <class 'tuple'>
