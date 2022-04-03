#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    first_diagonal = second_diagonal = 0
    # Time: O(n)
    # Space: O(1)
    for i in range(len(arr)):
        first_diagonal += arr[i][i]
        second_diagonal += arr[i][len(arr) - 1 - i]
    return abs(first_diagonal - second_diagonal)


if __name__ == '__main__':
    for i in range(10):
        print(~i)