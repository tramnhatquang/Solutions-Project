#!/bin/python3

import os

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

from heapq import *


def cookies(k, A):
	# Write your code here
	# append the element into the
	if not A:
		return -1
	heapify(A)  # O(n)
	count = 0
	while A[0] < k and len(A) > 1:
		smallest = heappop(A)  # O(1)
		second_smallest = heappop(A)  # O(1)
		heappush(A, smallest + second_smallest * 2)  # O(log N)
		count += 1

	# either A[0] >= k or len(A) <= 1
	if len(A) == 1 and A[0] < k:
		return -1
	return count


# time: O(n log n) where n is the length of the arr
# space: O(n) due


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	first_multiple_input = input().rstrip().split()

	n = int(first_multiple_input[0])

	k = int(first_multiple_input[1])

	A = list(map(int, input().rstrip().split()))

	result = cookies(k, A)

	fptr.write(str(result) + '\n')

	fptr.close()
