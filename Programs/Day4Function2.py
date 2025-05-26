# employees = [
#     {"name": "Riya", "salary": 50000},
#     {"name": "Ram", "salary": 60000},
#     {"name": "Charlie", "salary": 40000},
#     {"name": "Bob", "salary": 60000},
#     {"name": "David", "salary": 40000},
#     {"name": "Alice", "salary": 50000}
# ]

# # Sorting by salary, and then by name alphabetically
# sorted_employees = sorted(employees, key=lambda x: (-x["salary"], x["name"]))

# print(sorted_employees)

# # # Reduce
# from functools import reduce
# scores = [90, 85, 78, 92, 88]
# sum_of_scores = reduce(lambda x, y: x + y, scores)
# print(f"Sum of Scores: {sum_of_scores}")
 
 
# ## Recap Question 
# t = (1, 2, [3, 4, 5])
# t[2][2]=123
# print(t)
# t[2].append(6)  
# print(t)


# # Nested Functions
# def disp():
#     def show():
#        print("Hello, I Show function!")
#     print("Hello, I Disp function!")
#     show()
    
# disp()

# ## pass function as an argument
# def greet(name):
#     return f"Hello, {name} welcome!"

# def process_greeting(func, name):
#     greeting = func(name)
#     print(greeting)

# process_greeting(greet, "Alice")


# using Globals()
a = 50
def show () :
        a=89;
        print('Local Variable A:', a)
        x = globals()['a']
        #print('Global Variable A:{global a}')
        print('X:', x)
show()
print('Global Variable A:', a)

