def hello():
    print("Hello World")

greet = hello()
greet2 = hello
print(greet)  # None
print(greet2)  # <function hello at 0x7f8c4c3e1d30>
del hello
print(greet2())  # Hello World