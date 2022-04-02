# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # the iterative way
        #         prev, curr = None, head

        #         # Time: O(n), Space: O(1)
        #         while curr:
        #             nxt = curr.next
        #             curr.next = prev
        #             prev = curr
        #             curr = nxt
        #         return prev

        # the iterative way but using the construction, longer run-time
        # prev = None
        # while head:
        #     prev = ListNode(head.val, prev)
        #     head = head.next
        # return prev

        # the recursive way
        if (not head) or (not head.next):
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p