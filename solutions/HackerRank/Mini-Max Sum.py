#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    # Using the built-in function
    # arr = sorted(arr)
    # print(sum(arr[:-1]), sum(arr[1:]))

    # Not using the built-in function
    # Time: O(n)
    # Space: O(n)
    sum_arr = 0
    num_max = num_min = arr[0]
    for num in arr:
        sum_arr += num
        if num < num_min:
            num_min = num
        if num > num_max:
            num_max = num
    print(sum_arr - num_max, sum_arr - num_min)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
