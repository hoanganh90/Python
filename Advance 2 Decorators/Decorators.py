# Decorators: A decorator is a function that takes another function as an argument and 
# extends its behavior without explicitly modifying it.
# Decorators are a powerful and useful tool in Python that allows you 
# to modify the behavior of a function or class.
def hello():
    print("Hello World")

greet = hello() # Calling the function
greet2 = hello # Assigning the function to a variable
print(greet)  # None
print(greet2)  # <function hello at 0x7f8c4c3e1d30>
del hello
print(greet2())  # Hello World