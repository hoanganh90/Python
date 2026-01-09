def findNextGreaterElementsWithDistance(readings):
    # Write your code here
    result = []
    left = 0
    right = 1
    while True:
        tmp = [-1, -1]
        foundNextGreater = False
        for i in range(right, len(readings)):
            if readings[i] > readings[left]:
                tmp[0] = readings[i]
                tmp[1] = i - left
                result.append(tmp)
                left += 1
                right = left + 1
                foundNextGreater = True
                break
        if not foundNextGreater:
            result.append(tmp)
            left += 1
            right = left + 1
        if left == len(readings):
            break
    return result

def findNextGreater2(readings):
    n = len(readings)
    result = [[-1,-1] for _ in range(n)]
    stack = []
    for i in range(n):
        while stack and readings[i] > readings[stack[-1]]:
            index = stack.pop()
            result[index] = [readings[i], i - index]
        stack.append(i)
    return result
print(findNextGreaterElementsWithDistance([2, 1, 2, 4, 3]))
        

            
            
        
