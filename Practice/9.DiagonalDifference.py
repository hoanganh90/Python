def diagonalDifference(arr):
    # Write your code here
    size = len(arr)
    first_diagonal = 0
    second_diagonal = 0
    i = 0
    while(True):
        first_diagonal += arr[i][i]
        second_diagonal += arr[size - 1 - i][i]
        i += 1
        if(i == size):
            break
    return abs(first_diagonal - second_diagonal)
print(diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]]))