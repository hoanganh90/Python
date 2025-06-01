import re
test_1 = re.search('a', 'cat')  # Returns a match object
print(test_1)  # Output: <re.Match object; span=(0, 1), match='a'> The match occurred at the index 0 and ended at index 1
test_2 = re.search('a', 'dog')  # Returns None
print(test_2)  # Output: None