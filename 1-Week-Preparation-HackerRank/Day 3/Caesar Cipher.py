#!/bin/python3

import os


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s: str, k: int) -> str:
	# Write your code here
	# find the ASCII value of each character, add k into that value, and subtract ASCII value of 'A' if the letter is uppercase or subtract ASCII value of 'a' if the letter is lowercase
	char_list = []
	for char in s:
		# convert to its lowercase
		if char.isalpha():
			lower_char = char.lower()
			# wrapping around if the ascii value > 90 (lower_case)
			val = (ord(lower_char) + k - ord('a')) % 26

			# convert back to upper case if the original character is uppercase
			if char.isupper():
				char_list.append(chr(ord('A') + val))
			else:
				char_list.append(chr(ord('a') + val))
		else:
			# for non-letter characters
			char_list.append(char)

	return ''.join(char_list)


# time: O(n), n is the length of the string
# space: O(n)


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input().strip())

	s = input()

	k = int(input().strip())

	result = caesarCipher(s, k)

	fptr.write(result + '\n')

	fptr.close()
