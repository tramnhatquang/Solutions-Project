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
    hash_table = {}
    for i in a:
        if i not in hash_table:
            hash_table[i] = 1
        else:
            hash_table[i] += 1

    for key in hash_table:
        if hash_table[key] == 1:
            return key


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
