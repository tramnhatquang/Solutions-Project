from typing import *


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def preorder(self, root: TreeNode, target: int, buf: List[int], results:
	List[List[int]]) -> None:
		if not root:
			return

		target -= root.val
		buf.append(root.val)

		if target == 0 and not root.left and not root.right:
			results.append(buf[:])

		self.preorder(root.left, target, buf, results)
		self.preorder(root.right, target, buf, results)

		buf.pop()

	# time complexity: O(nlogh), n is number of nodes, h is the height of the tree
	# space complexity: O(nlogh)
	def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[
		List[int]]:
		if not root:
			return []

		results = []
		self.preorder(root, targetSum, [], results)

		return results


if __name__ == '__main__':
	s = Solution()
	root = TreeNode(5)
	# set-up the left subtree
	root.left = TreeNode(4)
	root.left.left = TreeNode(11)
	root.left.left.left = TreeNode(7)
	root.left.left.right = TreeNode(2)

	# setup the right subtree
	root.right = TreeNode(8)
	root.right.left = TreeNode(13)
	root.right.right = TreeNode(4)
	root.right.right.left = TreeNode(5)
	root.right.right.right = TreeNode(1)

	# call the function
	print(s.pathSum(root, 22))
