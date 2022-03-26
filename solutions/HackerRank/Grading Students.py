#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    # Time: O(n)
    # Space: O(1)
    # for i in range(len(grades)):
    #     if grades[i] < 38: continue
    #     next_multiple_5 = (grades[i] // 5 + 1) * 5
    #     if next_multiple_5 - grades[i] < 3:
    #         grades[i] = next_multiple_5
    # return grades

    # Another approach: Using the remainder
    # Time: O(n)
    # Space: O(1)

    for i in range(len(grades)):
        if grades[i] < 38:
            continue
        remainder = grades[i] % 5
        if 5 - remainder < 3:
            grades[i] += 5 - remainder
    return grades
