my_list = [1, 2, 3, 4, 5]
your_list = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
your_tuple = (6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
print(list(zip(my_list, your_list))) # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)] -> Pure function
print(list(zip(my_list, your_tuple))) # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)] -> Pure function