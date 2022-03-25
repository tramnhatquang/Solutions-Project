#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    # Time: O(n)
    # Space: O(1)
    arr.sort()
    length = len(arr)
    if length & 1:
        return arr[length//2]
    else:
        return arr[length//2] + arr[length//2 -1]
