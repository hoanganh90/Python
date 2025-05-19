def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        yield a
        temp = a
        a = b
        b = temp + b
for x in fibonacci(10):
    print(x)