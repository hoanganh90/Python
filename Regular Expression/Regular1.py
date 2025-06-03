import re
test_1 = re.search('a', 'cat')  # Returns a match object
print(test_1)  # Output: <re.Match object; span=(0, 1), match='a'> The match occurred at the index 0 and ended at index 1
print(test_1.span())  # Output: (0,1)
print(test_1.group())  # Output: 'a'
test_2 = re.search('a', 'dog')  # Returns None
print(test_2)  # Output: None

pattern = re.compile('search this inside of this text please!')
string = 'search this inside of this text please!'
a = pattern.search(string)  # Returns a match object
print(a)  # Output: <re.Match object; span=(0, 41), match='search this inside of this text please!'>
b = pattern.findall(string)  # Returns a list of all matches
print(b)  # Output: ['search this inside of this text please!']
c = pattern.match(string)  # Returns a match object if the string starts with the pattern
print(c)  # Output: <re.Match object; span=(0, 41), match='search this inside of this text please!'>
d = pattern.fullmatch(string)  # Returns a match object if the entire string matches the pattern
print(d)  # Output: <re.Match object; span=(0, 41), match='search this inside of this text please!'>

pattertnEmail = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
def is_valid_email(email):
    return bool(pattertnEmail.fullmatch(email))
# Example usage
print(is_valid_email('qwert@gmail.com'))