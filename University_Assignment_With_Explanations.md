
```python
from collections import defaultdict  # Import defaultdict to simplify course average calculations

# Step 1: Get user input to populate the nested dictionary
university_data = {}  # Main dictionary to store all student data

n = int(input("Enter number of students: "))  # Number of students to enter

for _ in range(n):  # Loop through each student
    student_id = input("Enter Student ID: ")  # Unique ID for the student
    name = input("Enter Name: ")  # Student's name
    major = input("Enter Major: ")  # Student's major (e.g., CS, Physics)

    # Initialize the student entry with name, major, and empty course dictionary
    university_data[student_id] = {
        "name": name,
        "major": major,
        "courses": {}
    }

    c = int(input(f"Enter number of courses for {name}: "))  # How many courses the student is taking
    for _ in range(c):  # Loop to input each course
        course = input("  Enter course name: ")  # Course name
        midterm = int(input("    Enter midterm score: "))  # Midterm score
        final = int(input("    Enter final score: "))  # Final exam score
        project = int(input("    Enter project score: "))  # Project score

        # Store scores in nested dictionary under course name
        university_data[student_id]["courses"][course] = {
            "midterm": midterm,
            "final": final,
            "project": project
        }

# Q1: Print all student names and their majors
print("\n--- Q1: All Student Names and Majors ---")
for student in university_data.values():
    print(f"{student['name']} - {student['major']}")

# Q2: Average score per course per student
print("\n--- Q2: Average Score per Course for Each Student ---")
for sid, details in university_data.items():
    print(f"\nStudent: {details['name']}")
    for course, scores in details["courses"].items():
        avg = sum(scores.values()) / len(scores)  # Calculate average of 3 scores
        print(f"  {course}: Avg Score = {avg:.2f}")

# Q3: Find students who scored >90 in final of Python101
print("\n--- Q3: Students with Final > 90 in Python101 ---")
for sid, details in university_data.items():
    course_data = details.get("courses", {}).get("Python101", {})
    if course_data.get("final", 0) > 90:
        print(f"{details['name']} scored {course_data['final']} in Python101 Final")

# Q4: Add new course AI101 for student S101
print("\n--- Q4: Add AI101 Course for a Student (S101 if exists) ---")
if "S101" in university_data:
    university_data["S101"]["courses"]["AI101"] = {"midterm": 89, "final": 94, "project": 91}
    print(f"Added AI101 to S101: {university_data['S101']['courses']['AI101']}")
else:
    print("Student S101 not found.")

# Q5: Remove Stats101 course from S102
print("\n--- Q5: Remove Stats101 Course from S102 ---")
if "S102" in university_data:
    removed = university_data["S102"]["courses"].pop("Stats101", None)  # Remove if exists
    print("Removed Stats101." if removed else "Stats101 not found.")
else:
    print("Student S102 not found.")

# Q6: Average score across all students for each course
print("\n--- Q6: Average Score of Each Course (All Students Combined) ---")
course_totals = defaultdict(lambda: {"sum": 0, "count": 0})  # Sum and count tracker

for student in university_data.values():
    for course, scores in student["courses"].items():
        for score in scores.values():
            course_totals[course]["sum"] += score
            course_totals[course]["count"] += 1

# Print average for each course
for course, data in course_totals.items():
    avg = data["sum"] / data["count"]
    print(f"{course}: Overall Avg = {avg:.2f}")

# Q7: Highest average in Math201
print("\n--- Q7: Top Student in Math201 ---")
highest_avg = 0
top_student = ""

for student in university_data.values():
    math_scores = student["courses"].get("Math201")
    if math_scores:
        avg = sum(math_scores.values()) / len(math_scores)
        if avg > highest_avg:
            highest_avg = avg
            top_student = student["name"]

if top_student:
    print(f"Top student in Math201: {top_student} with avg {highest_avg:.2f}")
else:
    print("No student found for Math201.")
```
