#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here

    # Brute-force solution
    # Time: O(n^2)
    # Space: O(1)
    # count = 0
    # for i in range(n - 1):
    #     for j in range(i + 1, n):
    #         if (ar[i] + ar[j]) % k == 0:
    #             count += 1
    # return count

    # More efficient solution: Written by snnikam01 in the discussion post
    # His HackerRank profile: https://www.hackerrank.com/snnikam01?hr_r=1
    # Time: O(n)
    # Space: O(1)
    freq = [0] * k
    ans = 0
    for i in ar:
        rem = i % k
        ans += freq[(k - rem) % k]
        # print(ans)
        freq[rem] += 1
        # print(freq)
    return ans

