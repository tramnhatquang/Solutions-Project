#!/bin/python3

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
from typing import *


def swap(arr: List[int], index1: int, index2: int) -> None:
	# swap two numbers at the given indices
	arr[index1], arr[index2] = arr[index2], arr[index1]


def minimumBribes(arr: List[int]) -> None:
	# Write your code here
	num_bribes = 0

	# loop the arr backward
	for i in range(len(arr) - 1, -1, -1):
		# if there are bribes happening at this index
		if arr[i] != i + 1:

			# if there is only one bribe
			if i - 1 >= 0 and arr[i - 1] == i + 1:
				num_bribes += 1
				swap(arr, i, i - 1)
			# if there are two bribes
			elif i - 2 >= 0 and arr[i - 2] == i + 1:
				num_bribes += 2
				swap(arr, i - 2, i - 1)
				swap(arr, i - 1, i)
			else:
				# there are more than 2 bribes
				print('Too chaotic')
				return

	print(num_bribes)


# time: O(n), n is the length of the arr
# space: O(1)


if __name__ == '__main__':
	t = int(input().strip())

	for t_itr in range(t):
		n = int(input().strip())

		q = list(map(int, input().rstrip().split()))

		minimumBribes(q)
