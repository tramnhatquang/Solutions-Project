from singly_linked_list import *

if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    head = linked_list.insert_node_at_tail(12)
    head = linked_list.insert_node_at_tail(21)
    head = linked_list.insert_node_at_tail(1)
    head = linked_list.insert_node_at_tail(5)
    head = linked_list.insert_node_at_head(100)
    head = linked_list.insert_node_at_head(101)
    head = linked_list.insert_node_at_head(102)
    print_linked_list(head)
    print(length(head))