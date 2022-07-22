# !/bin/python3

import os


#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
	# Write your code here
	A = 1000000000 + 7
	r = [0] * (m + 1)
	a = [0] * (m + 1)

	a[0] = 1
	for j in range(1, m + 1):
		a[j] += a[j - 1] if j - 1 >= 0 else 0
		a[j] += a[j - 2] if j - 2 >= 0 else 0
		a[j] += a[j - 3] if j - 3 >= 0 else 0
		a[j] += a[j - 4] if j - 4 >= 0 else 0
	for j in range(1, m + 1):
		a[j] = a[j] % A
		a[j] = a[j] ** n
		a[j] = a[j] % A

	r[1] = 1
	for j in range(2, m + 1):
		r[j] = a[j]
		for k in range(1, j):
			r[j] -= r[k] * a[j - k]
		r[j] = r[j] % A
	return r[m] % A


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	t = int(input().strip())

	for t_itr in range(t):
		first_multiple_input = input().rstrip().split()

		n = int(first_multiple_input[0])

		m = int(first_multiple_input[1])

		result = legoBlocks(n, m)

		fptr.write(str(result) + '\n')

	fptr.close()
