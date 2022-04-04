#
# Complete the 'getNode' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER positionFromTail
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def getNode(llist, positionFromTail):
    # Write your code here
    # Time: O(n) where n is the list's length
    # Space: O(n)
    # lst = []

    # while llist:
    #     lst.insert(0, llist.data)
    #     llist = llist.next

    # return lst[positionFromTail]

    # More elegant code where we save more space
    # Time: O(n), Space: O(1)
    current = res = llist
    idx = 0
    while current:
        current = current.next
        if idx > positionFromTail:
            res = res.next
        idx += 1
    return res.data
