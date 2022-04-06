#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
# Time complexity: O(n)
# Space complexity: O(n)
def lonelyinteger(a):
    # Write your code here
    # Time: O(n)
    # hash_table = {}
    # for i in a:
    #     if i not in hash_table:
    #         hash_table[i] = 1
    #     else:
    #         hash_table[i] += 1
    #
    # for key in hash_table:
    #     if hash_table[key] == 1:
    #         return key

    # Alternative approach: Using built-in count
    # Time: O(n)
    # Space: O(1)
    # for num in a:
    #     if a.count(num) == 1:
    #         return num


    # Another approach: Using bit-wise XOR
    unique = a[0]
    for i in a:
        unique ^= i
    return unique

