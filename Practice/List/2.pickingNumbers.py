def findLongestSubArrayNumbers(a):
    # Write your code here
    results = []
    i = 0
    sliding_window = [a[i]]
    while True:
        if abs(a[i+1] - a[i]) <= 1:
            sliding_window.append(a[i + 1])
            i += 1
        else:
            results.append(len(sliding_window))
            sliding_window = [a[i+1]]
            i += 1
        if i == len(a) - 1:
            break
    return max(results)
def longest_subarray(nums):
    counts = dict()
    max_length = 0
    # Count the frequency of each element
    for x in nums:
        counts[x] = counts.get(x,0) + 1
    # Iterate through the unique numbers in the counter
    for x in counts:
        if x+1 in counts:
            current_length = counts[x] + counts[x+1]
            max_length = max(max_length, current_length)
        else:
            max_length = max(max_length, counts[x])
    return max_length
print(findLongestSubArrayNumbers([4,6,5,3,3,1]))
print(longest_subarray([4,6,5,3,3,1]))
