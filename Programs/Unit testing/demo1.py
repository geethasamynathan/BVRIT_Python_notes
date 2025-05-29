def get_weather(temp):
    if temp < 0:
        return "Freezing"
    elif 0 <= temp < 20:
        return "Cold"
    elif 20 <= temp < 30:
        return "Warm"
    else:
        return "Hot"
    

def add(num1,num2):
    return num1 + num2

def divide(num1,num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2