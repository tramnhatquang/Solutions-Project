#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(llist, data):
    # Write your code here
    # if the llist is empty or it only has one element
    if not llist or not llist.next:
        return llist

    new_node = DoublyLinkedListNode(data)

    # if the data needs to be inserted at the beginning
    if llist.data > data:
        new_node.next = llist
        llist.prev = new_node
        return new_node

    curr = llist
    while curr.next.data < data:
        curr = curr.next

    # curr is before the inserting node
    nxt_node = curr.next

    # update the new node and the previous node
    curr.next = new_node
    new_node.prev = curr

    # update the new node and the next node
    new_node.next = nxt_node
    nxt_node.prev = new_node

    return llist
