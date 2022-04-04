#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    # Write your code here
    # Time: O(n) where n is the length of A 
    # Space: O(n)
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return 'NO'
    return 'YES'


