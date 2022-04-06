#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    # Time: O(n)
    # Space: O(n)
    res = [0] * 100
    for num in arr:
        res[num] += 1
    return res
