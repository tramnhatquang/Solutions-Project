from collections import deque
"""
This Queue Class uses an array to implement
Time complexity for its operations

* enqueue() takes O(1)
* dequeue() takes O(1)
"""
class Queue_Deque:

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Takes in an item and inserts that item into the 0th index of the list
        that is representing the Queue.

        The runtime is O(1), or constant time
        """
        self.items.append(item)

    def dequeue(self):
        """Returns and removes the front-most item of the Queue, which is
        represented by the last item in the list.

        The runtime is O(1), or constant time, because indexing to the end of a
        list happens in constant time.
        """
        if self.items:
            return self.items.popleft()
        return None

    def peek(self):
        """Returns the last item in the list. which represents the front-most
        item in the Queue.

        The runtime is constant because we're just indexing to the last item of
        the list and returning the value found there.
        """

        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the size of the Queue, which is represent by the length of
        the list.

        The runtime is O(1), or constant time, because we're only returning the length."""
        return len(self.items)

    def is_empty(self):
        """Returns a Boolean value expressing whether or not the list
        representing the Queue is empty.

        Runs in constant time, because it's only checking for equality.
        """
        return self.items == []

