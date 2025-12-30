def getTotalX(a, b):
    # This is brute force approach
    count =0
    for i in range(1,101):
        if all(i%x==0 for x in a): 
            if all(y%i==0 for y in b):
                count+=1 
    return count
print(getTotalX([2,4], [16,32,96]))
    