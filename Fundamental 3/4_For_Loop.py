# For loop in string
for item in ' Hoang cong anh':
    print(item)
# For loop in a list
for item in ['Hoang', 'cong', 'anh']:
    print(item)
# For loop in a tuple -> Looks like a choocolate bar (----)
for item in ('Hoang', 'cong', 'anh'):
    print(item)

# For loop in a set
for item in {'Hoang', 'cong', 'anh'}:
    print(item)

# For loop in a dictionary
dictionary_0 = {
    "name": "John",
    "age": 30,
}
for value in dictionary_0.values():
    print(value)  # Output: John 30
    
for key in dictionary_0:
    print(dictionary_0[key]) 