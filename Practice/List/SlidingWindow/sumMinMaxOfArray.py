from collections import deque
# Given an array of both positive and negative integers, 
# the task is to compute sum of minimum and maximum elements of all sub-array of size k.
def sumOfSubArrayInOrder(array, k):
    n = len(array)
    i = 0
    j = 0
    result = 0
    while j< n-1:
        j = i + k - 1
        result += min(array[i: j]) + max(array[i:j])
        i +=1
    return result
# Sliding window
def sumOfSubArrayAll(array, k):
    min_dq = deque()
    max_dq = deque()
    total_sum = 0
    for i in range(len(array)):
        # Remove elements that are out of the current window
        if min_dq and min_dq[0] <= i - k:
            min_dq.popleft()
        if max_dq and max_dq[0] <= i - k:
            max_dq.popleft()
        
        # Maintain monotonic increasing order in min_dq
        # If new element is smaller than back, back is no longer useful
        while min_dq and array[min_dq[-1]] >= array[i]:
            min_dq.pop()

        # 3. Maintain monotonic decreasing order in max_dq
        # If new element is larger than back, back is no longer useful
        while max_dq and array[max_dq[-1]] <= array[i]:
            max_dq.pop()

        #4 add current element's index
        min_dq.append(i)
        max_dq.append(i)

        # 5 Start calculating the 1st window once it is full
        if i>= k-1:
            total_sum += array[min_dq[0]] + array[max_dq[0]]
    return total_sum
print(sumOfSubArrayAll([2, 5, -1, 7, -3, -1, -2], 4))