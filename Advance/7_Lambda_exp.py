my_list = [5 , 4 , 3]
print(list(map(lambda x: pow(x, 2), my_list))) # [25, 16, 9] -> Pure function

# Sorting
a_tuple = [(0,2), (4,3), (9,1), (10, -4)]
print(list(sorted(a_tuple, key=lambda x: x[1]))) # [(10, -4), (9, 1), (4, 3), (0, 2)] -> Pure function