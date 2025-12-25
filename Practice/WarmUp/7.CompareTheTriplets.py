import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    sumA = 0
    sumB = 0
    # Write your code here
    for i in range(0,3):
        if(a[i] > b[i]):
            sumA = sumA + 1
        elif(a[i] < b[i]):
            sumB = sumB + 1
    return [sumA, sumB]
print(compareTriplets([17, 28, 30], [99, 16, 8]))