my_file = open(r'File IO\test.txt', "w")
my_file.write("Hello World")
my_file.close()

my_file = open('File IO/test.txt', "r")
print(my_file.read())
my_file.close