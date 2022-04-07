# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    # Write your code here
    # if not llist:
    #     head = SinglyLinkedListNode(data)
    #     return head

    # the current head (llist) is not null here
    # there is no need to check the head is null since the new head will point to null if it is the only node in the list
    new_head = SinglyLinkedListNode(data)
    new_head.next = llist
    return new_head
