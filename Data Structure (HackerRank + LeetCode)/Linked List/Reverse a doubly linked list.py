#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def reverse(head):
    # Write your code here
    previous, current = None, head
    while current:
        nxt = current.next
        current.next = previous
        if previous:
            previous.prev = current
        previous = current
        current = nxt
    return previous
