#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

# The code is copied and pasted from https://www.hackerrank.com/challenges/30-bitwise-and/forum
# The author is Jekus, his 3 Months Interview Preparation account:https://www.hackerrank.com/Jekus
def bitwiseAnd(N, K):
    # Write your code here
    if (K-1) | K <= N:
        return K-1
    return K-2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
