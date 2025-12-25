
import math
import os
import random
import re
import sys
import numpy as np
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
        digit = int(str_a[i]) + int(str_b[i]) + next_extra
        if(digit > 10):
            result.append(digit - 10)
            next_extra = 1
        else:
            result.append(digit)
            next_extra = 0
    result2 = int("".join(map(str, result)))
    value_32 = np.int32(result2)
    print(value_32)

sum2BigNumbers(17,18)
def aVeryBigSum(ar):
    # Write your code here
    pass
