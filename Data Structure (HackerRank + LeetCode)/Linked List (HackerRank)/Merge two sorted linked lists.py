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
    prev = curr = SinglyListNode()
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next

    # At least one of l1 and l2 can still have nodes at this point, so connect
    # the non-null list to the end of the merged list.
    prev.next = l1 or l2