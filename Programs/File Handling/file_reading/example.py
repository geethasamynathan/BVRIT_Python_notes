# Example: File Reading using read(), readline(), and readlines()

filename = "example.txt"

# 1. Using read()
with open(filename, "r") as file:
    print("Using read():")
    print(file.read())

# 2. Using readline()
with open(filename, "r") as file:
    print("\nUsing readline():")
    print(file.readline())
    print(file.readline())
    print(file.readline())

# 3. Using readlines()
with open(filename, "r") as file:
    print("\nUsing readlines():")
    lines = file.readlines()
    for line in lines:
        print(line.strip())
