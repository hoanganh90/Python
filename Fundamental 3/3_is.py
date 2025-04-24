print(True is True) # True is equal to True
print('1' is 1) # True is not equal to 1
print ([] is []) # [] is not equal to []. This is because lists are mutable and each time you create a new list, it is a new object in memory.
print ({} is {}) # {} is not equal to {}. This is because dictionaries are mutable and each time you create a new dictionary, it is a new object in memory.
print ([1,2,3] is [1,2,3]) # [1,2,3] is not equal to [1,2,3]. This is because lists are mutable and each time you create a new list, it is a new object in memory. 
a = 19
b = 19
print (a is b) # 19 is equal to 19. This is because integers are immutable and each time you create a new integer, it is the same object in memory.

# == is used to compare the values of two objects