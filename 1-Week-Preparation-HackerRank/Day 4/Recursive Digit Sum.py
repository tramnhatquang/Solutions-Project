#!/bin/python3

import os


#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n: str, k: int) -> int:
	# Write your code here
	def sum_digit(number: int) -> int:
		if number < 10:  # base case
			return number

		total = sum(int(i) for i in str(number))
		return sum_digit(total)

	convert_num = sum_digit(int(n))
	return sum_digit(convert_num * k)


# time: O(n log n). For each iteration, we reduce one digit which reduces log(n) time and call the repeated recursion for n times
# spacE: O(n)


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	first_multiple_input = input().rstrip().split()

	n = first_multiple_input[0]

	k = int(first_multiple_input[1])

	result = superDigit(n, k)

	fptr.write(str(result) + '\n')

	fptr.close()
