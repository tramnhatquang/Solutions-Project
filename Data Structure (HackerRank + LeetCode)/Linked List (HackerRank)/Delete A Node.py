def deleteNode(head, position):
    # Write your code here
    # delete the head which is the only node in the linked list
    # if position == 0:
    #     if not llist: # if the head is None
    #         return None
    #     else: # update the head if there are more than one in the list
    #         head = llist.next
    #         llist.next = None
    #         return head

    # current = llist
    # count = 1
    # while count < position and current:
    #     count += 1
    #     current = current.next

    # current.next = current.next.next
    # return llist

    current = head
    # next will point to None if there is
    # not another item in the list
    if position == 0:
        head = head.next
    else:
        # iterate to the right node
        for i in range(position - 1):
            current = current.next
        # and alter the next pointer
        current.next = current.next.next
    return head
