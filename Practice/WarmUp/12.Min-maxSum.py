def miniMaxSum(arr):
    arr.sort()
    min = arr[0] + arr[1] + arr[2] + arr[3]
    max = arr[0] + arr[1] + arr[2] + arr[3]
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                 for h in range(k+1, len(arr)):
                    sum = arr[i] + arr[j] + arr[k] + arr[h]
                    if sum <= min:
                        min = sum
                    if sum >= max:
                        max = sum
    print(f"{min} {max}")
miniMaxSum([1,5,3,9,7])
