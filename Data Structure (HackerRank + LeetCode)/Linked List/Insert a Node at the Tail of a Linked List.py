# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    if not head:
        head = SinglyLinkedListNode(data)
        return head

    # head is not Null here
    current = head
    while current.next:
        current = current.next

    current.next = SinglyLinkedListNode(data)
    return head
