#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Write your code here
    # brute-force solution
    # Time: O(n)
    # Space: O(1)
    count = [0 for _ in range(len(queries))]
    for index, query in enumerate(queries):
        count[index] = strings.count(query)
    return count
