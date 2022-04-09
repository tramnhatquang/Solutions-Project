"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def inOrder(root):
    #Write your code here
    ## The recursive way:
    # Time: O(n)
    # Space: O(n) due to the increasing of stack frames
    if root:
        inOrder(root.left)
        print(root.info, end = ' ')
        inOrder(root.right)

    # underlying principle: visit left subtree -> root -> right subtree
    ## The recursive way
    # Time: O(n)
    # Space: O(n) due to the number of nodes stored into the stack
    if not root:
        return

    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print(root.info, end=' ')
        root = root.right
