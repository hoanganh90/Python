# List in Python = Array in C++
li = [1,2,3,4,5]
li2 = ['_','a','2','b','ä','ö','c','d','e', 'A']
li3 = [1,2,3,'a','b','c']
# Data structure: a way to arrange data in computer programming

#List slicing
string = 'helloooooo'
string[0::2] # 'he' 0 to 2, 1 step
print(string[0::2])
# String is immutable, so we cannot change the value of a list
# List is mutable, so we cannot change the value of a list
li[0] = 10
li2.sort()
print(li2)  
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l1_odd = l1[0::2]
l2_even = l2[1::2]
l1_odd.extend(l2_even)
print(l1_odd)
list1 = [54, 44, 27, 79, 91, 41]

the_4th_index = list1.pop(4)
print(the_4th_index)
list1.insert(2, the_4th_index)
print(list1)
list1.append(the_4th_index)
print(list1)

#Exercise 4: Count the occurrence of each element from a list
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
sample_list_set = set(sample_list)
print(sample_list_set)
for i in sample_list_set:
    count = 0
    for j in sample_list:
        if i == j:
            count += 1
    print(f"{i}: {count}")