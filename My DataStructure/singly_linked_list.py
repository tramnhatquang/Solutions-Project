class Node:
	"""
	A basic implementation of a Node class
	"""

	def __init__(self, val: int = 0, next=None):
		self.val = val
		self.next = next


class SinglyLinkedList:
	"""
	A basic implementation of a Singly LinkedList class
	"""
	def __init__(self):
		self.head = None

	def insert_node_at_head(self, val: int) -> Node:
		"""
		Insert the node to the head of linked list
		:param val: (int) the inserted value
		:return: reference to the new head
		"""

		# Time: O(n) where n is the number of nodes in the linked list
		# Space: O(1)
		new_head = Node(val)
		new_head.next = self.head
		self.head = new_head
		return self.head

	def insert_node_at_tail(self, val: int) -> Node:
		"""
		Insert the node to the tail of linked list
		:param val: (int) the inserted value
		:return: reference to the head
		"""
		# Time: O(n) where n is the number of nodes in the linked list
		# Space: O(1)
		new_node = Node(val)

		# Check if the head is None
		if not self.head:
			self.head = new_node
			return self.head

		curr = self.head
		while curr.next:  # find the last node
			curr = curr.next

		curr.next = new_node
		return self.head

	def reverse_linked_list_iterative(self, head) -> Node:
		"""
		Reverse the whole linked list iteratively
		:param head: the reference to the head
		:return: the reference to the new head of reversed linked list
		"""
		prev, curr = None, head

		while curr:
			next_node = curr.next
			curr.next = prev
			prev = curr
			curr = next_node
		return prev

	def reverse_linked_list_recursive(self, head) -> Node:
		"""
		Reverse the whole linked list recursively
		:param head: the reference to the head
		:return: the reference to the new head of reversed linked list
		"""
		if not head or not head.next:
			return head

		new_head = self.reverse_linked_list_recursive(head.next)
		head.next.next = head
		head.next = None
		return new_head

	def contains_node_with_value(self, val: int) -> bool:
		"""
		Check whether a node with given value in the singly linked list
		:param val: the given value
		:return: True if found. Otherwise, returns False
		"""
		curr = self.head
		while curr and curr.val != val:
			curr = curr.next
		return curr is not None

def length(head: Node) -> int:
	curr = head
	count = 0
	while curr:
		count += 1
		curr = curr.next
	return count

def print_linked_list(head: Node) -> None:
	"""
	Prints out the whole linked list to console
	:param head: reference to head of linked list
	:return: None
	"""
	curr = head
	while curr:
		print(curr.val, end=' -> ')
		if not curr.next:
			print('None')
		curr = curr.next


def delete_duplicates(head: Node) -> Node:
	"""
	Delete duplicates in a sorted linked list
	:param head: reference to head of linked list
	:return: head: reference to the head of linked list
	"""
	curr = head
	while curr and curr.next:
		if curr.val == curr.next.val:
			curr.next = curr.next.next
		else:
			curr = curr.next
	return head
