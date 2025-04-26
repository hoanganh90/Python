# Enumerate
for char in enumerate("hello"):
    print(char)

for(index, char) in enumerate("hello"):
    print(index, char)


for(index, num) in enumerate([2,4,2,4,5,3,4,5,32,4,22,42,2]):
    print(index, num)