# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        curr = prev = head
        while curr:
            mCount = m
            nCount = n
            while curr and mCount != 0:
                prev = curr
                curr = curr.next
                mCount -= 1

            while curr and nCount != 0:
                curr = curr.next
                nCount -= 1

            prev.next = curr

        return head



