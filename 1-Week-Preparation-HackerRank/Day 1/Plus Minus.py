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
	zeroes_count = positive_count = 0
	for num in arr:
		if num > 0:
			positive_count += 1
		elif num == 0:
			zeroes_count += 1
	# ratio of positive numbers
	print(f'{positive_count / len(arr) : .6f}')
	print(f'{(len(arr) - positive_count - zeroes_count) / len(arr) : .6f}')
	print(f'{zeroes_count / len(arr) : .6f}')


# time: O(n), n is the length of the arr
# space: O(1)


if __name__ == '__main__':
	n = int(input().strip())

	arr = list(map(int, input().rstrip().split()))

	plusMinus(arr)
