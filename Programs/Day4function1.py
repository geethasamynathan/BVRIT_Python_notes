def Multiply():
    result=10*4.5
    return result

answer=Multiply()
print(answer)

def greet():
    return "Fucntion without args and without return "
    
#message=greet()
print(greet())  # This will print None because the function does not return anything.
# This function prints a greeting message.



## Example for Function with parameters and return value
def greet_with_name(name): # name is a parameter
    return f"welcome to  {name} "

message=greet_with_name("Capgemini") # Here, "Capgemini" is an argument passed to the function greet_with_name.
print(message)  # This will print the greeting message with the provided name.


# Example for Function with default parameters
def greet_with_default(name,location="Hyderabad",companyName="Capgemini"):  # name has a default value
    return f"Hi, {name} welcome to {companyName} {location}"

print(greet_with_default("John"))  # This will use the default values for location and companyName
print(greet_with_default("John", "New York"))  # This will use the default value for companyName
print(greet_with_default("Tim", "Liverpool", "Boeing"))  # This will override the default value for companyName
print(greet_with_default(name="Tim", companyName="Deloitte USA"))  # This will use the default value for location


# Example for Function with variable number of arguments
def getemployeeinfo(name,age):  # *skills allows for a variable number of arguments
    return f"Employee Name: {name}, Age: {age}"


print(getemployeeinfo("John", 30)) 
print(getemployeeinfo(age=45,name='Lalitha'))# This will print the employee information with the provided name and age


scores = [90, 85, 78, 92, 88]

def analyze_scores(scores):
    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)
    return total, average, highest, lowest
    
total_score,average_score,higest_score,lowest_score = analyze_scores(scores)
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score}")
print(f"Highest Score: {higest_score}")
print(f"Lowest Score: {lowest_score}")