def staircase(n):
    result = []
    row = 0
    while(True):
        temp_arr = []
        for i in range(0,n):
            if i >= n-row-1:
                temp_arr.append("#")
            else: temp_arr.append(" ")
        row += 1
        result.append(temp_arr)
        print("".join(map(str, temp_arr[::1])))
        if row == n:
            break
    #print(result)
staircase(6)
