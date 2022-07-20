class Node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class MyCircularQueue:

	def __init__(self, k: int):
		"""
		Initialize your data structure here. Set the size of the queue to be k.
		"""
		self.capacity = k
		self.count = 0
		self.head = None
		self.tail = None

	def enQueue(self, value: int) -> bool:
		"""
		Insert an element into the circular queue. Return true if the operation is successful.
		"""
		if self.isFull():
			return False
		if self.isEmpty():
			self.head = Node(value)
			self.tail = self.head
		else:
			new_node = Node(value)
			self.tail.next = new_node
			self.tail = new_node
		self.count += 1
		return True

	def deQueue(self) -> bool:
		"""
		Delete an element from the circular queue. Return true if the operation is successful.
		"""
		if self.isEmpty():
			return False
		self.head = self.head.next
		self.count -= 1
		return True

	def Front(self) -> int:
		"""
		Get the front item from the queue.
		"""
		if self.isEmpty():
			return -1
		return self.head.val

	def Rear(self) -> int:
		"""
		Get the last item from the queue.
		"""
		if self.isEmpty():
			return -1
		return self.tail.val

	def isEmpty(self) -> bool:
		"""
		Checks whether the circular queue is empty or not.
		"""
		return self.count == 0

	def isFull(self) -> bool:
		"""
		Checks whether the circular queue is full or not.
		"""
		return self.count == self.capacity

