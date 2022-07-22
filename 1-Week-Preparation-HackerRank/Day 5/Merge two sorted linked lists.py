#!/bin/python3

import sys


class SinglyLinkedListNode:
	def __init__(self, node_data):
		self.data = node_data
		self.next = None


class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert_node(self, node_data):
		node = SinglyLinkedListNode(node_data)

		if not self.head:
			self.head = node
		else:
			self.tail.next = node

		self.tail = node


def print_singly_linked_list(node, sep, fptr):
	while node:
		fptr.write(str(node.data))

		node = node.next

		if node:
			fptr.write(sep)


# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2) -> SinglyLinkedListNode:
	# DO IT ITERATIVELY

	# create a dummy node to keep track of the head's reference
	# sentinel = SinglyLinkedListNode(0)
	# curr = sentinel

	# # create two pointers pointing to the head of each LL
	# p1, p2 = head1, head2
	# while p1 and p2:
	#     if p1.data < p2.data:
	#         curr.next = SinglyLinkedListNode(p1.data)
	#         p1 = p1.next
	#     else:
	#         # p1.data >= p2.data
	#         curr.next = SinglyLinkedListNode(p2.data)
	#         p2 = p2.next
	#     curr = curr.next

	# # if one of the linked list is NOne, we connect the curr.next to the remaining of the non-None LL
	# curr.next  = p1 or p2
	# return sentinel.next

	sys.setrecursionlimit(1000000)
	# DO IT RECURSIVELY
	# establish the base cases
	p1, p2 = head1, head2

	if not p1:
		return p2
	if not p2:
		return p1

	# both heads are not None
	if p1.data < p2.data:
		p1.next = mergeLists(p1.next, p2)
		return p1
	else:
		p2.next = mergeLists(p1, p2.next)
		return p2
