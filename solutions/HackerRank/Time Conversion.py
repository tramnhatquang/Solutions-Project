#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# Time: O(1)
# Space: O(1)
def timeConversion(s):
    # Write your code here
    ## First approach
    # time = s[-2]
    # res = ''
    # if time == 'A':
    #     if s[:2] == '12':
    #         res += '00' + s[2:-2]
    #     else:
    #         res = s[:-2]
    # else:
    #     if int(s[:2]) < 12:
    #         res += str(int(s[:2]) + 12) + s[2:-2]
    #     else:
    #         res = s[:-2]
    # return res

    ## More elegant code
    if s.endswith('AM'):
        return '00' + s[2:-2] if s[:2] == '12' else s[:-2]

    return str(12 + int(s[:2]) % 12) + s[2:-2]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
