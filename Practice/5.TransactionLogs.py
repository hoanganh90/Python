#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold
#

def processLogs(logs, threshold):
    # Write your code here
    collection = []
    for log in logs:
        numbers = list(map(int, log.split()))
        first_and_second = numbers[:2]
        collection = collection + first_and_second
    set_collection = set(collection)
    dict_collection = dict()
    for item in set_collection:
        count_item = 0
        for i in range(0, len(collection), 2):
            if collection[i] == item or collection[i+1] == item:
                count_item = count_item + 1
        dict_collection[item] = count_item
    result = [str(key) for key, value in dict_collection.items() if value >= threshold]
    return result
result = processLogs(["9 7 50","22 7 20","33 7 50","22 7 30"],3)
print(result)