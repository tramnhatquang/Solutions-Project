# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # curr, lst = head, []
        # while curr: # traversing all the nodes, recording its value into a list
        #     lst.append(curr.val)
        #     curr = curr.next
        # # print(lst)
        # res, length = 0, len(lst)
        # # convering a binary number into a decimal
        # for k, v in enumerate(lst):
        #     res += 2**(length-1-k) * v
        # return res

        # A shorter, cleaner code using binary representation
        # since the linked list is not empty
        # res = head.val
        # while head.next:
        #     res = res * 2 +head.next.val
        #     head = head.next
        # return res

        # An alternative approach using binary manipulation
        res = 0
        while head:
            res = (res << 1) | head.val
            head = head.next
        return res