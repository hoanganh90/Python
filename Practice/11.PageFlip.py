def pageCount(n, p):
    # Write your code here
    right_count = 0
    i = 1
    last_page = n
    while (i < n):
        if i < p:
            i += 2
            right_count += 1
        else:
            break
    left_count = n // 2 - right_count
    return min(left_count, right_count)
print(pageCount(6,2))

