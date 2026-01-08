def getTopKFrequentEvents(events, k):
    # Write your code here
    events_dict = {}
    for x in events:
        events_dict[x] = events_dict.get(x, 0) + 1

    # From the order inside events_dict find the
    count = 0
    reversed_values_sorted_dict = [v for _,v in sorted(events_dict.items(), key= lambda item: item[1], reverse=True)[:k]]
    result = []
    while count < k:    
        for key,v in events_dict.items():
            if v == reversed_values_sorted_dict[count]:
                result.append(key)
                del events_dict[key]
                break
        count += 1
    return result

print(getTopKFrequentEvents([4, 4, 1, 2, 2, 3, 1, 3, 2], 3))