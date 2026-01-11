def countUniqueElements( array ):
    data_dict = dict()
    for x in array:
        data_dict[x] = data_dict.get(x, 0) + 1
    return data_dict
def countDistrictElement(array, k):
    i, j = 0, 0
    n = len(array)
    result = []
    while j < n:
        j = i + k
        new_map = countUniqueElements(array[i:j])
        result.append(len(new_map))
        i +=1
    return result
print(countDistrictElement([1, 2, 1, 3, 4, 2, 3],4))
