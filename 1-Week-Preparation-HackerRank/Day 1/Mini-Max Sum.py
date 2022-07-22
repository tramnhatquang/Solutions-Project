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

def miniMaxSum(arr) -> None:
	# Write your code here
	arr.sort()

	# find the min sum by adding the first four numbers
	min_sum = sum(arr[:4])

	# find the max sum by adding the last four numbers
	max_sum = sum(arr[1:])
	print(min_sum, max_sum)


if __name__ == '__main__':
	arr = list(map(int, input().rstrip().split()))

	miniMaxSum(arr)
