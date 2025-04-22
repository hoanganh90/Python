# Dictionary: A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
dictionary_0 = {
    "name": "John",
    "age": 30,
}
print(dictionary_0)  # Output: {'name': 'John', 'age': 30}
print(dictionary_0["name"])  # Output: John
# A dictionary has no order, so the order of the items may not be the same as the order in which they were added.
dictionary = {
    'weapon': 'sword',
    'greeting': 'hello',
    'isMagic': True,
    True: "Hello",
    123: [123, 456],
    'age': 30,
}

# A key is mutable -> Cannot be changed. -> Cannot add a list as a key.
print(dictionary['weapon'])  # Output: sword
print(dictionary.get('greeting2'))  # Output: None but the program will not crash
print(dictionary.get('greeting')) # Output: hello
print(dictionary.get('age', 55)) # Output: 30. If age does not exist, it will return 55.
print(123 in dictionary) # Output: True. Check if the key exists in the dictionary.
print(dictionary.keys()) # Output: dict_keys(['weapon', 'greeting', 'isMagic', True, 123, 'age'])

user2 = dict(name= 'John', age = 30) # Defining a dictionary using the dict() constructor
print(user2) # Output: {'name': 'John', 'age': 30}
user2.clear()
print(user2) # Output: {}
