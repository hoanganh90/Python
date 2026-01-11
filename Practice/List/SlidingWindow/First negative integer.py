def findFirstNegativeInteger(array, k):
    from collections import deque
    left, right = 0, 0
    result = []
    while left < len(array) - k:
        right = left + k
        found = False
        for idx, x in enumerate(array[left: right]):
            if x < 0:
                result.append(x)
                found = True
                break
        if found == False:
            result.append(0)
        left += 1
    return result
print(findFirstNegativeInteger([-8, 2, 3, -6, 1], 2))
