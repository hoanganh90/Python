def findTheMissingPositiveInt(array):
    n = len(array)
    for i in range(n):
        while 1 <= array[i] <= n and array[array[i] - 1] != array[i]:
            # Swap arrya[i] with the element at its target position
            target_idx = array[i] - 1
            array[i], array[target_idx] = array[target_idx], array[i]
    for i in range(n):
        if array[i] != i + 1:
            return i + 1
    # If all numbers 1 to n are present
    return n + 1
print(findTheMissingPositiveInt([1, 14, 3, 1]))