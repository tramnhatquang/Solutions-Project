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
