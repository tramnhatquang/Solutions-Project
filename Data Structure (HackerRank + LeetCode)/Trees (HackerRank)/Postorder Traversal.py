"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def postOrder(root):
    #Write your code here
    ## Recursive Way:
    # Time: O(n)
    # Space: O(n) due to the increasing stack frames
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end = ' ')

    ## Iterative Way:
    if not root:
        return
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.info)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    while res:
        print(res.pop(), end=' ')