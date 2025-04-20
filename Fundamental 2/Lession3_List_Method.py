basket = [ 1, 2, 3,4,5,6,7,8,9]
# Adding to a list - APPEND
basket.append(10) 

# Inserting to a list - INSERT
basket.insert(0, 10)
print(basket) 

#Extending a list - EXTEND
basket.extend([11, 12, 13])
print(basket)

# Removing from a list - REMOVE
basket.remove(10)  # Remove the 1st occurrence of 10

basket.pop(4)  # Remove the 4th index element (5)
print(basket) 