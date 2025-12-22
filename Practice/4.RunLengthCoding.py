def LengthEncoding(input_str):
    set_str = set(input_str)
    print(set_str)
    result = ""
    for item in set_str:
        print(str(input_str.count(item))+item)
        result = result + str(input_str.count(item))+item
    print(result)
LengthEncoding("aaaabbccc")
example_set = {"a", 2, "c", 4, "b", 6}
popped_element = example_set.pop()
print(popped_element)
print(example_set)