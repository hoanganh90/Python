my_list = [1, 2, 3, 4, 5]
def multiply_by2(item):
    return item * 2
print(list(map(multiply_by2, my_list))) # [2, 4, 6, 8, 10] -> Pure function
print(list(my_list)) # [1, 2, 3, 4, 5] -> Pure function    