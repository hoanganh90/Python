
import math
import os
import random
import re
import sys
#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#
def sum2BigNumbers (a,b):
    str_a = str(a)[::-1]
    str_b = str(b)[::-1]
    result_len = len(str_a) if len(str_a) > len(str_b) else len(str_b)
    result = []
    digit = 0
    next_extra = 0
    for i in range(0, result_len):
        val_a = int(str_a[i]) if i < len(str_a) else 0
        val_b = int(str_b[i]) if i < len(str_b) else 0
        digit = val_a + val_b + next_extra
        if(digit >= 10):
            result.append(digit - 10)
            next_extra = 1
        else:
            result.append(digit)
            next_extra = 0
    if next_extra == 1:
        result.append(next_extra)
    result2 = int("".join(map(str, result[::-1])))
    #value_32 = np.int32(result2)
    return result2
def aVeryBigSum(ar):
    # Write your code here
    result = 0
    for i in range(0,len(ar)):
        result = sum2BigNumbers(result, ar[i])
    return result
print(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005  ]))
