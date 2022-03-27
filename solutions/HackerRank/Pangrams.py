#!/bin/python3

import math
import os
import random
import re
import sys
import string


# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):

    # Write your code here
    # Time: O(n)
    # Space: O(1)
    alphabet = string.ascii_lowercase + ' '
    s = ''.join(set(s.lower()))
    for char in alphabet:
        if char not in s:
            return 'not pangram'

    return 'pangram'
