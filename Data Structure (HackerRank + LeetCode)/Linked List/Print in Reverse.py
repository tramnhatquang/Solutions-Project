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
