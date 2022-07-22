#!/bin/python3

import os


#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
	# Write your code here
	# since the arr is odd, the median number is equal to arr[len(arr) // 2] after sorting
	# sort the arr
	arr.sort()
	return arr[len(arr) // 2]


# time: O(n log n) due to sorting
# space: O(n) due to sorting

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input().strip())

	arr = list(map(int, input().rstrip().split()))

	result = findMedian(arr)

	fptr.write(str(result) + '\n')

	fptr.close()
