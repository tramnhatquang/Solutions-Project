#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#
# Time: O(n)
# Space: O(1)
def breakingRecords(scores):
    # Write your code here
    res = [0, 0]
    max_num = min_num = scores[0]
    for num in scores:
        if num > max_num:
            max_num = num
            res[0] += 1
        elif num < min_num:
            min_num = num
            res[1] += 1

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
