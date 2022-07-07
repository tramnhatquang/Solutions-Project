class MinStack:

	def __init__(self):
		self.arr = []
		self.min = []

	def push(self, val: int) -> None:
		self.arr.append(val)
		min_val = min(val, self.min[-1] if self.min else val)
		self.min.append(min_val)

	def pop(self) -> None:
		if self.arr and self.min:
			self.arr.pop()
			self.min.pop()

	def top(self) -> int:
		return self.arr[-1]

	def getMin(self) -> int:
		return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()