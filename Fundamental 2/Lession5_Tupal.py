# Tuple: is a collection of objects that are ordered and UNCHANGABLE. All data stay in the same order.
my_tupal = ( 1, 2, 3, 4, 5)
print(my_tupal)
print(5 in my_tupal)
print(my_tupal[3] )
# Tupal can be added as a key to a dictionary because it is unchangable
my_dict = { (1, 2): "Hello", (3, 4): "World"}
print(my_dict[(1, 2)])
print(my_tupal[2: 5]) # Slicing items in a tupal
x,y,z, *others = my_tupal # Unpacking tupal
print(others)
print(len(others)) # Count the number of items in a tupal
print(others.count(4)) # Count the number of items in a tupal - 1
print(my_tupal.index(4)) # What the index of 4 in the tupal
