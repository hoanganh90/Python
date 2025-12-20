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
user3 = user2.copy()
user2.clear()
print(user2) # Output: {}
print(user3) # Output: {'name': 'John', 'age': 30}
user3.update({'name': 'Jane'})
print(user3.get('name')) # Output: Jane

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
my_dict['country'] = 'USA' # This will add the key-value pair to the dictionary.
print(my_dict) # Output: {'name': 'Alice', 'age': 35, 'city': 'New York', 'country': 'USA'}
# Delete an item from a dict
del my_dict['name']
print(my_dict)
# POP an item from a dict
my_dict.pop("age")
print(my_dict)
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
my_dict.popitem()
print(my_dict)

#Exercise 9: Modify Nested Dictionary
nested_student_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(f"Nested dictionary: {nested_student_dict}")
# Change the value name by call the key
nested_student_dict['class']['student']['name'] = "Jessica"
# Print new dict
print(f"New nested dict: {nested_student_dict}")

# Exercise 11: Create a dictionary by extracting the keys from a give dict
sample_dict = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New York"
}
keys = ["name", "salary"]
new_dict = { k: sample_dict[k] for k in keys}
print("New dict is: " , new_dict)