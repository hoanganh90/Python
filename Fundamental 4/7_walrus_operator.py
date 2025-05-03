# := walrus operator
# The walrus operator (:=) is used to assign a value to a variable as part of an expression.
some_list = [-1, -2, -3, -4, -5]
if n := len(some_list) > 0:
    print(f"List has {n} elements")

a = 'helooooooooooo'
if len(a) > 10:
    print(f"String is too long: {len(a)} characters")
if (n:=len(a)) > 10:
    print(f"String is too long: {n} characters")