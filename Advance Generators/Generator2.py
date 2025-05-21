# interable
# iterate
# genrators


def generator_function(num):
    for i in range(num):
        yield i * 2
    
# The generator function is a special type of function that uses the "yield" statement to produce a series of values.
print(generator_function(10))
for item in generator_function(10):
    print(item) # items are generated one at a time

def generator_function2(num):
    for i in range(num):
        yield i*2
g = generator_function2(10)
print(g) # <generator object generator_function2 at 0x7f8c1c0e3b50>
next(g) # next() is used to get the next value from the generator
print(next(g)) # get the next value from the generator  2                  
print(next(g)) # get the next value from the generator 4
print(next(g)) # get the next value from the generator 6
print(next(g)) # get the next value from the generator 8

# next() will raise a StopIteration exception when there are no more values to generate