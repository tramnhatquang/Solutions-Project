class Node:
	"""
	A basic implementation of a Node class
	"""

	def __init__(self, value, prev=None, next=None):
		self.value = value
		self.prev = None
		self.next = None


class DoublyLinkedList:
	"""
	A basic implementation of a Doubly LinkedList class
	"""

	def __int__(self):
		self.head = None
		self.tail = None
