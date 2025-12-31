def migratoryBirds(arr):
    # Write your code here
    set_arr = set(arr)
    dict_arr = {}
    for item in set_arr:
        dict_arr[item] = arr.count(item)
    # 1. Find the maximum value in the dictionary
    max_value = max(dict_arr.values()) # Result: 3

    # 2. Get all keys that have this maximum value
    max_keys = [key for key, value in dict_arr.items() if value == max_value] # Result: [4, 5]

    # 3. Find the minimum key among those with the max value
    result_key = min(max_keys) # Result: 4
    print(result_key)
migratoryBirds([1,4,4,4,5,3])
