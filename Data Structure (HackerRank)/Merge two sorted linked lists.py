#!/bin/python3

import math
import os
import random
import re
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
def mergeLists(head1, head2):
    # Time complexity: O(N+M) where N is the length of head1, M is the length of head2
    # if not head1: # if head1 is null
    #     return head2
    # if not head2: # if head2 is null
    #     return head1
    # # if head1 and head2 are both null, the case is still applied to these conditions above

    # # finding the next node in the merged linked list
    # if head1.data < head2.data:
    #     head1.next = mergeLists(head1.next, head2)
    #     return head1
    # else:
    #     head2.next = mergeLists(head1, head2.next)
    #     return head2

    # using the iterative way

    # finding the head of the merged linked list and increase the pointer
    if head1.data < head2.data:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next

    current = head
    # while both linked lists still have data
    while head1 and head2:
        # merge the lower value node
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next

        # update the next pointer
        current = current.next
    # At here, one of the lists is NULL
    # if one of the lists still have data
    if head1:
        current.next = head1
    else:
        current.next = head2

    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
