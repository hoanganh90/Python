# Decorator: A function that takes another function as an argument and extends its behavior without explicitly modifying it.
def hello():
    print("Hello World")
def my_decorator(func):
    def wrap_func():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrap_func

@my_decorator # This is a decorator
def hello():
    print("Hello World")

hello()  # Hello World