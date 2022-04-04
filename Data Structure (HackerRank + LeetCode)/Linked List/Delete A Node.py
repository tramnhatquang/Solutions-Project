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


#
# Complete the 'deleteNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(head, position):
    # Write your code here
    # delete the head which is the only node in the linked list
    # if position == 0:
    #     if not llist: # if the head is None
    #         return None
    #     else: # update the head if there are more than one in the list
    #         head = llist.next
    #         llist.next = None
    #         return head

    # current = llist
    # count = 1
    # while count < position and current:
    #     count += 1
    #     current = current.next

    # current.next = current.next.next
    # return llist

    current = head
    # next will point to None if there is
    # not another item in the list
    if position == 0:
        head = head.next
    else:
        # iterate to the right node
        for i in range(position - 1):
            current = current.next
        # and alter the next pointer
        current.next = current.next.next
    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, ' ', fptr)
    fptr.write('\n')

    fptr.close()
