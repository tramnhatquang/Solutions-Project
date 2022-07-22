#!/bin/python3

import os

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#
from collections import defaultdict


def pairs(k, arr):
	# Write your code here
	seen = defaultdict(int)
	count = 0
	for num in arr:
		count += seen[num - k] + seen[num + k]
		seen[num] += 1

	return count


# time: O(n), space: O(n)

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	first_multiple_input = input().rstrip().split()

	n = int(first_multiple_input[0])

	k = int(first_multiple_input[1])

	arr = list(map(int, input().rstrip().split()))

	result = pairs(k, arr)

	fptr.write(str(result) + '\n')

	fptr.close()
