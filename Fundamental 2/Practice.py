#Exercise 1: Perform Basic Tuple Operations
my_tuple = (1, 2, 3, 4, 5)
#Access and print the third element of my_tuple

print(my_tuple[3])
print(len(my_tuple))
# Exercise 2: Tuple Repetition *
print(my_tuple * 3)
# Exercise 3: Slicing Tuples
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sliced_numbers = numbers[4:7]
print(sliced_numbers)
# Ex 4: Reverse tuple
reversed_numbers = numbers[::-1]
print(reversed_numbers)
# Exercise 5: Access Nested Tuples
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])
# Exercise 11: Function Returning Tuple
def get_min_max(numbers):
    # Write your code here
    numbers.sort()
    return (numbers[0], numbers[-1])
def get_min_max_2(numbers):
    # Write your code here
    return (min(numbers), max(numbers))
# Test the function
my_numbers = [10, 5, 20, 2, 15]
min_max_values = get_min_max_2(my_numbers)
print(f"Original numbers: {my_numbers}")
print(f"Minimum and maximum values: {min_max_values}")

# Exercise 13: Removing Duplicates from Tuple
my_tuple = (1, 2, 2, 3, 4, 4, 5)
new_tuple_set = set(my_tuple)
new_tuple = tuple(new_tuple_set)
print(f"new non duplicate tuple: {new_tuple}")

students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 95)]
print(f"Original student list: {students}")

high_achievers_loop = []
for student in students:
  if student[1] >= 90:
    high_achievers_loop.append(student)
print(f"Students with scores 90 or above (loop method): {high_achievers_loop}")