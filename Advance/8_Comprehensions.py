# list set dictionay comprehensions
# List Comprehensions
# [expression for item in iterable]
# [expression for item in iterable if condition]
# [expression for item in iterable if condition1 and condition2]
# [expression for item in iterable if condition1 or condition2]
# [expression for item in iterable if condition1 and not condition2]
# [expression for item in iterable if condition1 or not condition2]
# [expression for item in iterable if not condition1 and condition2]
# [expression for item in iterable if not condition1 or condition2]
# [expression for item in iterable if not condition1 and not condition2]
# [expression for item in iterable if not condition1 or not condition2]
# [expression for item in iterable if not condition1 and not condition2]
# [expression for item in iterable if not condition1 or not condition2]
# [expression for item in iterable if not condition1 and not condition2]
# [expression for item in iterable if not condition1 or not condition2]
# [expression for item in iterable if not condition1 and not condition2]
# [expression for item in iterable if not condition1 or not condition2]
# [expression for item in iterable if not condition1 and not condition2]

my_list = [5, 4, 3]
for char in 'hello':
    my_list.append(char)
print(my_list)  # [5, 4, 3, 'h', 'e', 'l', 'l', 'o']
# List Comprehensions
my_list = [ char for char in 'hello' ]
print(my_list)  # for param in 'hello' ]

my_list = [ char for char in 'hello' if char != 'l' ]
print(my_list)  # ['h', 'e', 'o']

my_list = [ num for num in range(0,100) if num %3 == 0 and num %5 == 0]
print(my_list)  # [0, 15, 30, 45, 60, 75, 90]

my_set = { num for num in range(0, 19 ) if num % 2 == 0 }
print(my_set)  # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

my_dict = { num: num**2 for num in range(0, 10) }
print(my_dict)  #

some_list = ['a', 'b', 'c', 'b', 'a', 'n', 'o', 'a']
set_duplicates = set([ char for char in some_list if some_list.count(char) > 1 ])
print([set_duplicates])  # ['a', 'b'])   