#!/bin/python3

import os

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#
from typing import *


def gridChallenge(grid: List[List[str]]) -> str:
	# Write your code here

	# sort each row in the grid and append it to a new arr
	# Loop over each column, check two consecutive pairs at the same column. If they are not in alphabetical order, return 'NO'. Otherwise, continue the loop until we reach the end.

	ROWS, COLS = len(grid), len(grid[0])
	new_grid = []
	for row in grid:
		new_grid.append(''.join(sorted(row)))

	for col in range(COLS):
		for row in range(ROWS - 1):
			if new_grid[row][col] > new_grid[row + 1][col]:
				return 'NO'
	return 'YES'


# time: O(n^2 log n)
# space: O(n)


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	t = int(input().strip())

	for t_itr in range(t):
		n = int(input().strip())

		grid = []

		for _ in range(n):
			grid_item = input()
			grid.append(grid_item)

		result = gridChallenge(grid)

		fptr.write(result + '\n')

	fptr.close()
