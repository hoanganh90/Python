def generateAngleBracketSequences(n):
    # Write your code here
    i = 0
    result = [""]
    count_items= 0
    while True:
        for j in range(count_items,len(result)):
            tmp_left = "<>" +  result[j]
            tmp_right = result[j] + "<>"
            tmp_center = "<" + result[j] + ">"
            if tmp_left == tmp_right:
                result.append(tmp_left)
                count_items +=1
            else:
                result.append(tmp_left)
                result.append(tmp_right)
                count_items +=2
            if tmp_left != tmp_center:
                result.append(tmp_center)
                count_items +=1
        result = result[len(result) - count_items:]
        count_items = 0
        i += 1
        if i>= n:
            break 
    return result
print(generateAngleBracketSequences(4))
