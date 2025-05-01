def say_Hello():
    print("Hello World")
    return # The function say_Hello() is defined to print "Hello World" to the console.
# say_Hello() # This will print "Hello World" to the console.
say_Hello()

# Exercise 1
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
def showTree(picture: list):
    for row in picture:
        for pixel in row:
            if(pixel == 1):
                print("*", end="") #When you set end="", 
                # it prevents the newline from being added and instead appends an empty string ("") after the output. 
                # This allows the next print() call to continue on the same line.
            else:
                print(" ", end="")
        print("")
    return # The function showTree() is defined to print a tree-like structure using a 2D list (picture) of 0s and 1s.
showTree(picture) 

#parameter: a value that is passed into a function when it is called.
def say_hello2(name, emoji):
    print(f'Hello {name} {emoji}')

#passing arguments to the function
say_hello2("John", "😊") 
say_hello2( "😊","John") 
# Function with keyword arguments
say_hello2(emoji="😊",name = "Anh")