"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    #Write your code here
    ## The recursive way
    # Time: O(n)
    # Space: O(n) due to the increasing of stack frames which could be up to
    # n nodes
    if root:
        print(root.info, end = ' ')
        preOrder(root.left)
        preOrder(root.right)

    ## The iterative way:
    # Time: O(n)
    # Space: O(n) due to the number of nodes stored into the stack
    stack = [root]
    if not root:
        return

    while stack:
        node = stack.pop()
        print(node.info, end=' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)