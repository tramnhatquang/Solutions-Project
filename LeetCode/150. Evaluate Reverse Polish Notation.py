from typing import List
class Solution:
	def evalRPN(self, tokens: List[str]) -> int:
		stack = []

		for char in tokens:
			if char not in ['+', '-', '*', '/']:
				stack.append(char)
			else:
				num2, num1 = int(stack.pop()), int(stack.pop())
				if char == '+':
					stack.append(num1 + num2)
				elif char == '-':
					stack.append(num1 - num2)
				elif char == '*':
					stack.append(num1 * num2)
				else:
					if num1 > 0 and num2 >0:
						stack.append(num1 // num2)
					else:
						stack.append(num1 / num2)
		# the last element in the stack is the result
		return stack[-1]


if __name__ == '__main__':
	print(int(5 / 2))