def multiplication_or_sum(num1, num2):
    # Calulate the product
    product = num1 * num2
    if product > 1000:
        return num1 + num2
    else:
        return product
print(multiplication_or_sum(40,30))
# Ex2 Print the Sum of a Current Number and a Previous number
def Sum_oF_current_and_past(num):
    print("Printing current and previous number and their sum in a range({num})")
    previous_num = 0
    # Loop
    for i in range(1,num):
        x_sum = previous_num + i
        print('Current Number ', i , 'Prevous Number ', previous_num, 'Sum: ', x_sum)
        previous_num = i
print(Sum_oF_current_and_past(10))

# Ex3: Print characters present at an even index number
def Print_Even_Index_value(str):
    print("Original string is ", str)
    print("Printing onlu even index chars:")
    for i in range(0, len(str) - 1):
        if i%2 == 0:
            print(str[i])
    for i in range(0, len(str)- 1, 2):
        print(str[i])
# Test
Print_Even_Index_value("PYnative")
#Exercise 4: Remove first n characters from a string
def remove_first_n_chars(n, str):
    new_str = str[n:]
    print(new_str)
remove_first_n_chars(3, "qwertyuio")
#Exercise 5: Check if the first and last numbers of a list are the same
def verifyTheFirstAndLastNumbers(arr):
    return print(arr[0] == arr[len(arr)-1])
verifyTheFirstAndLastNumbers( [75, 65, 35, 75, 30])
#Exercise 7: Find the number of occurrences of a substring in a string
def findNumOfOccurrences(str, keyword):
    count = str.count(keyword)
    print(keyword, "appeared ",count, " times")
findNumOfOccurrences("Emma is good developer. Emma is a writer", "Emma")
#Exercise 9: Check Palindrome Number
def checkPalindrome(num):
    if num < 0:
        return False
    original_string = str(num)
    reversed_string = original_string[::-1]
    return print(original_string == reversed_string)
checkPalindrome(12321)
# Exercise 10: Merge two lists using the following condition
def MergeTwoLists(list1, list2):
    new_list_1 = list1[1:len(list1):2]
    new_list_2 = list2[0:len(list2):2]
    new_merged_list = new_list_1 + new_list_2
    print(new_merged_list)
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
MergeTwoLists(list1,list2)