#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(num_towers, tower_height) -> int:
	# Write your code here
	# SInce both players play optimally, each player would like to make the height of 1 of whatever the tower it chooses
	# because 1 evenly devides by all other numbers. The answer depends on the number of towers being odd or even
	# except for the case when the tower height is equal to 1, player 1 will always lose
	if tower_height == 1:
		return 2
	else:
		if num_towers % 2 == 0:
			return 2
		else:
			return 1


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	t = int(input().strip())

	for t_itr in range(t):
		first_multiple_input = input().rstrip().split()

		n = int(first_multiple_input[0])

		m = int(first_multiple_input[1])

		result = towerBreakers(n, m)

		fptr.write(str(result) + '\n')

	fptr.close()
