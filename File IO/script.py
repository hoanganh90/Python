my_file = open(r'File IO\test.txt', "w")
my_file.write("Hello World")
my_file.close()

my_file = open('File IO/test.txt', "r")
print(my_file.read())
my_file.close

with open('File IO/test.txt', "r") as my_file:
    print(my_file.read())
with open('File IO/test.txt', "w") as my_file_w:
    my_file_w.write("Hello World 2")
with open('File IO/test.txt', "r+") as my_file_rw:
    my_file_rw.write("Hello World 3")
with open('File IO/test.txt', "r") as my_file:
    print(my_file.read())   