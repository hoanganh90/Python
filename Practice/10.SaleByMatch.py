def sockMerchant(n, ar):
    # Write your code here
    set_ar = set(ar)
    dict_arr = dict()
    for item in set_ar:
        dict_arr[item] = ar.count(item)
    count_pairs = 0
    for sock_amount in dict_arr.values():
        if sock_amount > 1:
            count_pairs += sock_amount // 2
    return count_pairs
sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20])