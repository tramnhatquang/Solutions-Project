#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    # Time: O(n)
    # Space: O(1)
    sea_level = valley_counter = 0
    for step in path:
        if step == 'D' and sea_level == 0:
            valley_counter += 1
        sea_level += 1 if step == 'U' else -1
    return valley_counter

