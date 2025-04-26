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
    "city": "New York",
    "country": "USA"

}
for value in dictionary_0.values():
    print(value)  # Output: John 30
    
for key in dictionary_0:
    print(dictionary_0[key]) 

for item in dictionary_0.items():
    print(item)  
for key in dictionary_0.keys():
    print(key) 
for item in dictionary_0.items():
    key, value = item
    print(key, value )  
for key, value in dictionary_0.items():
    print(key, value )  