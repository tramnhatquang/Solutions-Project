## My self-implementation for Singly-Linked List (HackerRank)
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data) -> None:
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        return self.head


    def print_singly_linked_list(self) -> None:
        curr = self.head
        while curr:
            print(curr.data, ' -> ', end='')
            if not curr.next:
                print('None')
            curr = curr.next

    def insert_at_head(self, val) -> None:
        new_node = SinglyLinkedListNode(val)
        if not self.head:  # if the head is None
            self.head = new_node

        # the head is not None
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, val) -> None:
        new_node = SinglyLinkedListNode(val)
        # if head is None and head is also tail
        if not self.head:
            self.head = new_node

        # head is not None
        curr = self.head
        while curr.next:  # traversing to the current tail of the linked list
            curr = curr.next

        curr.next = new_node


    def reverse_linked_list(self, head):
        if not head or not head.next:
            return head

        p = self.reverse_linked_list(head.next)
        head.next.next = head
        head.next = None
        return p

if __name__ == '__main__':
    singly_linked_list = SinglyLinkedList()
    head = singly_linked_list.insert_node(12)
    head = singly_linked_list.insert_node(23)
    head = singly_linked_list.insert_node(345)
    head = singly_linked_list.insert_node(56)
    head = singly_linked_list.print_singly_linked_list()
    tail = singly_linked_list.reverse_linked_list(head)
    singly_linked_list.print_singly_linked_list()