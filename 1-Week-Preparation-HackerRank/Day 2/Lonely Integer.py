#!/bin/python3

import os
from typing import *


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(arr: List[int]) -> int:
	# Write your code here
	# approach: Hash table
	# 1. We loop over the array and record the occurences of each value. After finish the loop, go over the table and return the element whose occurence is one
	# table = collections.Counter(arr)
	# for k, v in table.items():
	#     if v == 1:
	#         return k

	# return -1 # if not found
	# time = space = O(n), n is the length of the arr

	# approach 2: ^-XOR operator to reduce the space complexity
	# a ^ a = 0
	# 0 ^ b = b
	ans = 0
	for num in arr:
		ans ^= num
	return ans


# time: O(n), space: O(1)


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input().strip())

	a = list(map(int, input().rstrip().split()))

	result = lonelyinteger(a)

	fptr.write(str(result) + '\n')

	fptr.close()
