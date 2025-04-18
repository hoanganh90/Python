# string concatenation
print('hello' + ' world')
print('hello' + '5')
#print('hello' + 5 ) # TypeError: can only concatenate str (not "int") to str
print(str(199))
# Esacape sequence
weather  = 'It\'s sunny'
print(weather)
weather2  = 'It\'s \"kind of\" sunny'
print(weather2)

weather3  = '\t It\'s \"kind of\" \n sunny'
print(weather3)

# Formatted string literals (f-strings)

name = 'Jonny'
age = 55
print(f'Hi {name}, you are {age} years old')
print(' Hi {}, you are {} years old'.format(name, age))