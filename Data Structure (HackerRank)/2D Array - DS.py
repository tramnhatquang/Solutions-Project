#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    # assign the min negative inf for max_sum
    max_sum = float('-inf')

    # Time: O(n^2) where n is the length of the given array
    for i in range(4):
        for j in range(4):
            total = 0
            total += arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][
                j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            if total > max_sum: max_sum = total
    return max_sum

