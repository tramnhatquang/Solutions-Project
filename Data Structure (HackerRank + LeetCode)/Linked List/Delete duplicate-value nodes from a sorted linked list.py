#
# Complete the 'removeDuplicates' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
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
def traverseLinkedList(head):
    while head:
        print(head.data, '->', end='')
        if not head.next:
            print('NULL')
        head = head.next


def removeDuplicates(head):
    # Write your code here
    # Time: O(n) where n is the length of the linked list
    # check if the list is empty
    if not head:
        return head

    # the distinct value will possibly start from the second val
    curr = head
    while curr.next:
        if curr.next.data == curr.data:
            # temp = curr.next
            curr.next = curr.next.next
            # temp.next = None
        else:
            curr = curr.next

    return head
