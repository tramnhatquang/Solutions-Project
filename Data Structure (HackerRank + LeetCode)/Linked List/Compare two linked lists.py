# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    # curr1, curr2 = llist1, llist2
    # while curr1 and curr2:
    #     if curr1.data != curr2.data:
    #         return 0
    #     curr1 = curr1.next
    #     curr2 = curr2.next

    # if not curr1 and  not curr2: # both current pointers are None
    #     return 1
    # return 0

    # much more elegant code
    # the last part is to compare whether two pointers pointing to NULL if they both reach the end of two linked lists
    while (llist1 and llist2 and llist1.data == llist2.data):
        llist1 = llist1.next
        llist2 = llist2.next
    return llist1 == llist2
