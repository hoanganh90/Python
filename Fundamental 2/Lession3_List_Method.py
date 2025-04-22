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
print(basket.index(8))  # Get the index of 8
print (2 in basket)
print(basket.count(2))
# Cannot print out basket.sort() because it returns None
# Sorting a list - SORT
basket.sort() # Create a new list with the sorted values
print(basket) 
basket.reverse() # Create a new list with the sorted values
print(basket)  # Sort the list in ascending order

# None: is a special data type which is similar to null in other programming languages
