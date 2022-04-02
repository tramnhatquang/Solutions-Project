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


def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')


#
# Complete the 'reversePrint' function below.
#
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reversePrint(llist):
    # Write your code here, using a list
    # lst = []
    # current = llist
    # if current: # the list is not empty
    #     while current:
    #         lst.insert(0, current.data)
    #         current = current.next
    # print('\n'.join(map(str, lst)))

    # using a stack
    # stack = []
    # if llist:
    #     current = llist
    #     while current:
    #         stack.append(current.data)
    #         current = current.next
    #     while len(stack) != 0:
    #         print(stack.pop())

    # using a recursion
    if not llist:  # the base-case
        return
    if llist:
        reversePrint(llist.next)
        print(llist.data)


if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        reversePrint(llist.head)
