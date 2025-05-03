max = 0
def highest_event(li):
    max = li[0]
    for i in li:
        if i > max:
            max = i
    return max
        
def highest_even(li):
    even = []
    for i in li:
        if i%2 == 0:
            even.append(i)
    return max(even)

print(highest_event([10,2,3,4,8]) )  # [10,2,3,4,8] => 10
print(highest_event([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5] => 5