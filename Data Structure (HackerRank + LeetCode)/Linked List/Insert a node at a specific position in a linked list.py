# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    # Write your code here
    current = llist

    if position == 0:
        current = SinglyLinkedListNode(data)
        current.next = llist
        return current

    # the given head is not None and we have valid insertion
    count = 1  # counting the head

    while count < position and current:
        current = current.next
        count += 1

    # at here, we are at the previous node before the inserting node
    new_node = SinglyLinkedListNode(data)
    new_node.next = current.next
    current.next = new_node
    return llist
