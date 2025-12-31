def countingValleys(steps, path):
    # Write your code here
    inValley = False
    height = 0
    step = 0
    count_valley = 0
    while step < steps:
        if path[step] == 'U':
            height += 1
           
        elif path[step] == 'D':
            height -= 1
        if height >= 0 and inValley == True:
            inValley = False
            count_valley += 1
        if height < 0 and inValley == False:
            inValley = True
        step += 1
    return count_valley
print(countingValleys(12,"DDUUDDUDUUUD"))
            