class MyCircularQueue:

	def __init__(self, k: int):
		self.head, self.tail = 0, 0
		self.arr = [0] * k  # declare an array of length k
		self.size = k

	def enQueue(self, value: int) -> bool:
		# if the queue is not full, we enqueue a new value
		if not self.isFull:
			self.arr[self.tail] = value
			self.tail = (self.tail + 1) % self.size
			return True
		return False

	def deQueue(self) -> bool:
		# if the queue is not empty, we can dequeue the front item
		if not self.isEmpty():
			self.head = (self.head + 1) % self.size
			return True
		return False

	def Front(self) -> int:
		return -1 if self.isEmpty() else self.arr[self.head]

	def Rear(self) -> int:
		return -1 if self.isEmpty() else self.arr[self.tail]

	def isEmpty(self) -> bool:
		return self.head == self.tail

	def isFull(self) -> bool:
		return (self.tail - self.head + 1) % self.size == 0

	def print(self):
		print(' '.join(map(str, self.arr)))

if __name__ == '__main__':
	queue = MyCircularQueue(5)
	assert queue.enQueue(12) is True
	queue.print()
	# print(queue)()
	print(queue)