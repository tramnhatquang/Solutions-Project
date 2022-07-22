#!/bin/python3

import os


#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s: str) -> str:
	# Write your code here
	open_to_close = {
		'(': ')',
		'[': ']',
		'{': '}'
	}
	stack = []
	for bracket in s:
		if bracket in open_to_close:
			stack.append(bracket)
		else:
			if stack and open_to_close[stack[-1]] == bracket:
				stack.pop()
			else:
				return 'NO'
	return 'YES' if not stack else 'NO'


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	t = int(input().strip())

	for t_itr in range(t):
		s = input()

		result = isBalanced(s)

		fptr.write(result + '\n')

	fptr.close()
