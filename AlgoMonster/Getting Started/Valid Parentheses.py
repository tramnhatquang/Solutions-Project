def valid_parentheses(s: str) -> bool:
	# WRITE YOUR BRILLIANT CODE HERE

	stack = []
	match = {'(': ')',
	         '[': ']',
	         '{': '}'}
	# Time: O(n)
	# Space: O(n) since the stack can contain at most n characters
	for char in s:
		if char in match:
			stack.append(char)
			continue
		else:
			if stack and match[stack.pop()] != char:
				return False
	return True if not stack else False



