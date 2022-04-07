# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1: We use a helper method to calculate the length of the
# linked list and retrieve the midpoint using basic math

        # size = self.length(head)
        # curr = head
        # for i in range(size // 2):
        #     curr = curr.next
        # return curr

        # Approach 2: Iterating each node and record its value into an array
# A. The middle node is A[A.length // 2] since we can retrieve each node by
# index
#         arr = [head]
#         while arr[-1].next:
#             arr.append(arr[-1].next)
#         return arr[len(arr) // 2]

        # Approach 3: Usingfast and slow pointer, make another pointer fast
        # that traverses twice as fast as slow. When fast reaches the end of
        # the list, slow must be in the middle
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

