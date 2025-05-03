# Scope: What variables are accessible where
# Scope refers to the visibility of variables in different parts of the code.
# In Python, variables have a scope that determines where they can be accessed.
# There are four types of scopes in Python:
# 1. Local Scope: Variables defined inside a function are local to that function.
# 2. Enclosing Scope: Variables defined in the enclosing function (if any) are accessible to inner functions.
# 3. Global Scope: Variables defined at the top level of a module are global and can be accessed anywhere in the module.
# 4. Built-in Scope: Names preassigned in the built-in names module are always available.

# 3. Global scope
total = 100 # Global variable. Can be accessed anywhere in the module.

def add_to_total(x):
    global total # Declare total as a global variable to modify it. 
    total = 0 # This will create a new local variable total which will shadow the global variable.
    # If you don't declare total as global, it will be treated as a local variable.
    total += x # Modify the global variable.

    #x: # This is a 1.Local variable, 
    #  4. Built-in Scope
    s = sum([4,5]) # sum is a built-in function.
    print(s) # Output: 9
    return total
print(add_to_total(50)) # Output: 150
print("Hello" == 'Hello') # Output: True
print("Hello"[0]) # Output: H