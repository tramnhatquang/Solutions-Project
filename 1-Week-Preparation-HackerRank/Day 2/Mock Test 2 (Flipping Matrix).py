#!/bin/python3

import os

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
from typing import *


def flippingMatrix(matrix: List[List[int]]) -> int:
	# Write your code here
	# apporach: for each cell in the top left sub-matrix (n x x), each cell can only be reversed to certain positions. For example, if n = 2, we have 4x4 matrix, cell [0][0] can only be reversed into position [3][0], [0][3], [3][3]. This happens to every cell in the top left corner
	# the general solution is that every m[i][j] from the top left quarter:
	# m[i][j] ⇌ m[i][(2n-1)-j] ⇌ m[(2n-1)-i][j] ⇌ m[(2n-1)-i][(2n-1)-j]

	res = 0
	actual_length = len(matrix)
	n = actual_length // 2
	for row in range(n):
		for col in range(n):
			res += max(matrix[row][col], matrix[row][actual_length - col - 1],
			           matrix[actual_length - row - 1][col],
			           matrix[actual_length - row - 1][actual_length - 1 - col])

	return res


# time: O(n^2), n is the length of the arr
# space: O(1)


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	q = int(input().strip())

	for q_itr in range(q):
		n = int(input().strip())

		matrix = []

		for _ in range(2 * n):
			matrix.append(list(map(int, input().rstrip().split())))

		result = flippingMatrix(matrix)

		fptr.write(str(result) + '\n')

	fptr.close()
