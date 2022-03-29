class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root) -> int:
        # Write your code here

        # if not root:
        #     return -1

        # left = self.getHeight(root.left)
        # right = self.getHeight(root.right)

        # if left > right:
        #     return left + 1
        # else:
        #     return right + 1
        if not root:
            return -1
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))


T = int(input())