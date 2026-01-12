def reverseIndividualWords(input):
    temp_stack = ""
    result = ""
    right = 0
    left  = 0
    while right < len(input):
        if input[right] == " " or right == len(input) - 1:
            temp_str = input[left: right][::-1]
            result = result + temp_str + " "
            left = right + 1
            right += 1
        else:
            right += 1
    return result
print(reverseIndividualWords("Hello World"))