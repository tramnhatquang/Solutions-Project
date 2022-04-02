#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Write your code here
    # Using the built-in function
    # return a[::-1]

    # Without using the data structure
    b = []
    for i in range(len(a) - 1, -1, -1):
        b.append(a[i])
    return b
