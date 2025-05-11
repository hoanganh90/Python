# Lambda expressions
# Lambda expressions are anonymous functions defined with the lambda keyword. They can take any number of arguments but can only have one expression. The expression is evaluated and returned when the lambda function is called. Lambda functions are often used for short, throwaway functions that are not reused elsewhere in the code.
# They are commonly used in functional programming, especially in conjunction with higher-order functions like map(), filter(), and reduce().   
# Lambda functions are often used for short, throwaway functions that are not reused elsewhere in the code.
# They are commonly used in functional programming, especially in conjunction with higher-order functions like map(), filter(), and reduce().
# Lambda functions are often used for short, throwaway functions that are not reused elsewhere in the code.
# WHen dev just want to use a function once, they can use lambda function instead of defining a function using def keyword.
from functools import reduce # Importing reduce from functools module to use it for reducing a list to a single value
lambda_func = lambda x: x + 1 # Lambda function that takes one argument and returns the argument plus 1
print(lambda_func(5)) # 6
my_list = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 2, my_list))) # [2, 4, 6, 8, 10] -> Pure function
print(list(filter(lambda x: x % 2 == 0, my_list))) # [2, 4] -> Pure function
print(list(map(lambda x: x * 2, my_list))) # [2, 4, 6, 8, 10] -> Pure function
print(reduce(lambda x, y: x + y, my_list)) # 15 -> Pure function