# Pure functions are functions that have the following properties:
# 1. Deterministic: Given the same input, a pure function will always return the same output. It does not depend on any external state or data.
# 2. No side effects - No Error: A pure function does not modify any external state or data. It does not perform any observable actions, such as modifying a global variable, writing to a file, or printing to the console.
# 3. Referential transparency: A pure function can be replaced with its output value without changing the program's behavior. This means that a pure function can be reasoned about in isolation from the rest of the program.
# Pure functions are easier to test, reason about, and parallelize. They are a key concept in functional programming and are often used in functional programming languages like Haskell and Lisp.
#                                                                   
def multiply_by2(li):
    new_list = []
    for i in li:
        new_list.append(i * 2)
    return new_list
print(multiply_by2([1, 2, 3, 4, 5])) # [2, 4, 6, 8, 10] -> Pure function
