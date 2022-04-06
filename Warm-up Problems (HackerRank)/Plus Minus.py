#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    # Time complexity: O(n)
    # Space complexity: O(1)
    length = len(arr)
    positive_count = 0
    zero_count = 0
    for i in arr:
        if i > 0:
            positive_count += 1
        elif i == 0:
            zero_count += 1
    # print(positive_count / length)
    print('{:.6f}'.format(positive_count / length), end='\n')
    print('{:.6f}'.format((length - positive_count - zero_count) / length),
          end='\n')
    print('{:.6f}'.format(zero_count / length), end='\n')
