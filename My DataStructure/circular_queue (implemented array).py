class CircularQueue:
    """
    A basic implementation of a Circular Queue
    # Time: O(1). All of the methods in the circular data structure is of
    constant time complexity
    # Space: O(n). The overall space complexity of the data structure is linear, where NN is the pre-assigned capacity of the queue. However, it is worth mentioning that the memory consumption of the data structure remains as its pre-assigned capacity during its entire life cycle.
    """

    def __init__(self, capacity: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = 0
        self.capacity = capacity
        self.arr = [0] * capacity
        self.head_index = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.arr[(self.head_index + self.size) % self.capacity] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.head_index = (self.head_index + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.arr[self.head_index]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.arr[(self.head_index + self.size - 1) % self.capacity]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.capacity == self.size

