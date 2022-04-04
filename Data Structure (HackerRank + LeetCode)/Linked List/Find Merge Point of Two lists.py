# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    curr1, curr2 = head1, head2
    while curr1 != curr2:
        if curr1.next:
            curr1 = curr1.next
        else:
            curr1 = head2

        if curr2.next:
            curr2 = curr2.next
        else:
            curr2 = head1

    return curr1.data
