# Method in Python is a function that is associated with an object. 
# Using the dot operator, we can call a method on an object.



# Functions are defined using the def keyword, 
# while methods are defined within a class and are called on instances of that class.


# Docstrings are a way to document your code and provide information about what a function or method does.
# They are enclosed in triple quotes and can be accessed using the __doc__ attribute of the function or method.
def test(a):
    '''
    This is a test function that takes an argument a and returns its square.
    '''
    print(a**2)
    return a**2
print(test.__doc__) # This will print the docstring of the test function.
print(test(5)) # This will print the square of 5, which is 25