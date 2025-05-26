
def my_decorator(func):
    def wrapper(**kwargs):
        print("Before the function call")
        result = func( **kwargs)
        print("After the function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name} welocme!")

greet(name="Geetha")