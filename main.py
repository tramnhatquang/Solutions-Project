from typing import *


# Definition for singly-linked list.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def inorder(root: TreeNode) -> List[int]:
	res = []

	def helper(root: TreeNode) -> None:
		if root:
			helper(root.left)
			res.append(root.val)
			helper(root.right)
	helper(root)
	return res


if __name__ == '__main__':
	root = TreeNode(5)
	root.left = TreeNode(4)
	root.left.left = TreeNode(2)
	root.right = TreeNode(10)
	root.right.left = TreeNode(8)

	res = inorder(root)
	print(res)
