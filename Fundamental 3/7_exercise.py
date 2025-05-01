# Exercise 1
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
for row in picture:
    for pixel in row:
        if(pixel == 1):
            print("*", end="") #When you set end="", 
            # it prevents the newline from being added and instead appends an empty string ("") after the output. 
            # This allows the next print() call to continue on the same line.
        else:
            print(" ", end="")
    print("")