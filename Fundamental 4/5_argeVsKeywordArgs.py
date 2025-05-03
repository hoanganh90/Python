# *arg and **kwarg - Star argument and double star argument(keyword argument)
# *args: allows you to pass a variable number of non-keyword arguments to a function
# **kwargs: allows you to pass a variable number of keyword arguments to a function
def super_func(*args, **kwargs):
    print(*args)  # Unpacking the list and printing each element
    print(kwargs)  # Printing the keyword arguments as a dictionary
    total = 0
    for item in kwargs.values():
       total += item
    print(f'total: ' + str(total))  # Printing the sum of the keyword arguments
    return sum(args)
sum = super_func(1, 2, 3, 4, 5, num1=5, num2=10)  # [1, 2, 3, 4, 5] => 15
print(sum)  # 15


# Rule: params, *args, default params, **kwargs