from collections import OrderedDict


class LRUCache:
    # Approach 1: Ordered Dictionary
    # Using the OrderedDict data structure from collections module
    # Time: O(1) for both put and get
    # Space: O(capacity)
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Move the value to the end
        self.cache.move_to_end(key)

        # Return the key's value
        return self.cache.get(key)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            self.size += 1
        self.cache[key] = value
        if self.size > self.capacity:
            self.cache.popitem(last=False)
            self.size -= 1

    ## Approach 2: Hashmap + Doubly Linked List
    # One advantage of double linked list is that the node can remove itself without other reference. In addition, it takes constant time to add and remove nodes from the head or tail.
    #
    # One particularity about the double linked list implemented here is that there are pseudo head and pseudo tail to mark the boundary, so that we don't need to check the null node during the update.
    class DoublyLinkedListNode:
        def __init__(self):
            self.key = 0
            self.value = 0
            self.next = None
            self.prev = None

    class LRUCache:

        def _add_node(self, node):
            """
            Always add node to the head
            """
            node.prev = self.head
            node.next = self.head.next

            self.head.next.prev = node
            self.head.next = node

        def _remove_node(self, node):
            """
            Remove an existing node from the linked list
            """
            prev = node.prev
            nxt = node.next

            prev.next = nxt
            nxt.prev = prev

        def _move_to_head(self, node):
            """
            Move certain node in between to the head
            """
            self._remove_node(node)
            self._add_node(node)

        def _pop_tail(self):
            """
            Pop the current tail
            """
            res = self.tail.prev
            self._remove_node(res)
            return res

        def __init__(self, capacity: int):
            self.head = DoublyLinkedListNode()
            self.tail = DoublyLinkedListNode()
            self.capacity = capacity
            self.cache = {}
            self.size = 0

            # Link the head and tail
            self.head.next = self.tail
            self.tail.prev = self.head

        def get(self, key: int) -> int:
            node = self.cache.get(key, None)
            if not node:
                return -1

            self._move_to_head(node)
            return node.value

        def put(self, key: int, value: int) -> None:
            node = self.cache.get(key)
            if not node:
                new_node = DoublyLinkedListNode()
                new_node.value = value
                new_node.key = key

                self.cache[key] = new_node
                self._add_node(new_node)

                self.size += 1
                if self.size > self.capacity:
                    # pop the tail
                    tail = self._pop_tail()
                    del self.cache[tail.key]
                    self.size -= 1


            else:  # node is already existed in the linked list
                node.value = value
                self._move_to_head(node)

    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)