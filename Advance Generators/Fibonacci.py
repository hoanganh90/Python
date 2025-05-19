def fibonacci(n): # This is a generator function. It is more memory efficient than the second one.
    a=0
    b=1
    for i in range(n):
        yield a
        temp = a
        a = b
        b = temp + b

def fibonacci_2(n): # This way is not recommended because it uses more memory
    a = 0
    b = 1
    result = []
    for i in range(n):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

for x in fibonacci(10):
    print(x)