import os
import shutil

# # Absolute Paths
# source_abs = r"C:\Personal\BVRIT Python\Notes Repo\BVRIT_Python_notes\Programs\File Handling\The-zen-of-python.txt"
# destination_abs = r"C:\Personal\Backup\data.txt"

# # Relative Paths (assuming you're in "project" folder)
# source_rel = "The-zen-of-python.txt"
# destination_rel = "..\\backup\\data.txt"

# # Copy using absolute path
# shutil.copy(source_abs, destination_abs)
# print("File copied using absolute path.")

# Relative Paths (assuming you're in "project" folder)
source_rel = ".\\writing"
destination_rel = "..\\backup1"

# # Copy using relative path
# shutil.copy(source_rel, destination_rel)
# print("File copied using relative path.")

# # Copytree using relative path
# shutil.copytree(source_rel, destination_rel)
# print("Files copied using relative path.")


# # Example to know the size of a file
import os
file_size=os.path.getsize("country1.csv")
print("Size of the file is",file_size,"bytes")