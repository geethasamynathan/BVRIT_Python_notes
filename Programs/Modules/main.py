# import math_utils
# def main():
#     num1=int(input("Enter first number: "))
#     num2=int(input("Enter second number: "))
#     print(f"Addition Result={math_utils.Addition(num1, num2)}")
#     print(f"Subtraction Result={math_utils.Subtraction(num1, num2)}")
#     print(f"Multiplication Result={math_utils.Multiplication(num1, num2)}")    
    
# main() 

# import math_utils as mymath
# def main():
#     num1=int(input("Enter first number: "))
#     num2=int(input("Enter second number: "))
#     print(f"Addition Result={mymath.Addition(num1, num2)}")
#     print(f"Subtraction Result={mymath.Subtraction(num1, num2)}")
#     print(f"Multiplication Result={mymath.Multiplication(num1, num2)}")    
    
# main()    
    
    
from math_utils import Addition, Subtraction
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
AdditionResult=Addition(num1, num2)
SubtractionResult=Subtraction(num1, num2)   
print(f"Addition Result={AdditionResult}")              
print(f"Subtraction Result={SubtractionResult}")

from math_utils import Addition as add, Subtraction as sub
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
AdditionResult=add(num1, num2)
SubtractionResult=sub(num1, num2)   
print(f"Addition Result={AdditionResult}")              
print(f"Subtraction Result={SubtractionResult}")


from math_utils import *
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
AdditionResult=Addition(num1, num2)
SubtractionResult=Subtraction(num1, num2)
MultiplicationResult=Multiplication(num1, num2)   
print(f"Addition Result={AdditionResult}")              
print(f"Subtraction Result={SubtractionResult}")
print(f"Multiplication Result={MultiplicationResult}")

