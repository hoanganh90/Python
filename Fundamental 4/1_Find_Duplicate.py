list = ['a', 'b', 'c', 'b', 'a', 'b', 'a', 'c', 'b', 'a', 'c', 'b', 'a', 'c', 'b', 'd', 'c', 'd', 'a']
duplicate = []
for value in list:
    if list.count(value) > 1:
        if value not in duplicate:
            duplicate.append(value)
print(duplicate)
