# While loop
# While loop is used to execute a block of code repeatedly as long as a given condition is true.
i = 0
while i < 5:
    i += 1
    print(i)
    break
else:
    print("Loop ended") # The else block is executed when the while loop condition becomes false.

# While True
while True:
    input(" Say something: ")
    break # The break statement is used to exit the loop.

while True:
    response = input("Say something: ")
    if(response == "exit"):
        break
    print("You said: " + response) 

#pass
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    pass
i = 0
while i < 5:
    print(i)
    i += 1
    pass # The pass statement is a null operation; it is syntactically required but does nothing.