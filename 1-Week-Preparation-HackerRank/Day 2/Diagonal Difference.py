#!/bin/python3

import os


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
	# Write your code here
	# Note that:
	# - Sum of the first diagonal is equal to arr[i][j] where i == j
	#   - Sum of the second diagonal is equal to arr[i][j] where j == n - 1 - i where n is the length of the square matrix

	# time: O(n^2)
	# space: O(1)

	# sum_first_diagonal = sum_second_diagonal = 0
	# n = len(arr)
	# for row in range(n):
	# 	for col in range(n):
	# 		if row == col:
	# 			sum_first_diagonal += arr[row][col]
	# 		if col == n - 1 - row:
	# 			sum_second_diagonal += arr[row][col]
	#
	# return abs(sum_first_diagonal - sum_second_diagonal)

	sum_first_diagonal = 0
	sum_second_diagonal = 0

	for i in range(0, len(arr)):
		sum_first_diagonal = sum_first_diagonal + arr[i][i]
		sum_second_diagonal = sum_second_diagonal + arr[i][len(arr) - 1 - i]

	return abs(sum_first_diagonal - sum_second_diagonal)


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input().strip())

	arr = []

	for _ in range(n):
		arr.append(list(map(int, input().rstrip().split())))

	result = diagonalDifference(arr)

	fptr.write(str(result) + '\n')

	fptr.close()
