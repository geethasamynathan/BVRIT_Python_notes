import os
import csv

# 1. List files
# print("Files:", os.listdir("."))
# os.chdir("..")  # Change to parent directory
# print("Changed directory to:", os.getcwd())
# print("Files:", os.listdir("."))

# # 2. Create and write a new file
# with open("newfile.txt", "w") as f:
#     f.write("Hello from Python!")

# # 3. Check existence
# if os.path.exists("newfile.txt"):
#     print("newfile.txt exists")

# # 4. Rename file
os.rename("..\\testfile1.txt", "renamedfile.txt")

# # 5. Delete file
# if os.path.exists("renamedfile.txt"):
#     os.remove("renamedfile.txt")
#     print("File deleted")

# # 6. Create and navigate directory
# os.makedirs("data_folder", exist_ok=True)
# os.chdir("data_folder")
# print("Current directory:", os.getcwd())

# # 7. Write CSV
# data = [
#     ["Name", "Age", "City"],
#     ["Alice", 30, "New York"],
#     ["Bob", 25, "London"]
# ]
# with open("sample.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# # 8. Read CSV
# with open("sample.csv", newline="") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print("Row:", row)
