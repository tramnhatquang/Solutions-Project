### Iterative Way
def insert(self, val):
    # Insert iteratively
    if not self.root:
        self.root = Node(val)
        return self.root

    curr = self.root
    while True:
        if curr.info <= val:
            if not curr.right:
                curr.right = Node(val)
                break
            else:
                curr = curr.right
        else:
            if not curr.left:
                curr.left = Node(val)
                break
            else:
                curr = curr.left
    return self.root

### Recursive Way
    # Time: O(log n)
    # Space: O(n)
    def insert(self, val):
        # Enter you code here.
        def helper(root, val):
            if not root:
                return Node(val)

            if root.info < val:
                root.right = helper(root.right, val)
            else:
                root.left = helper(root.left, val)
            return root

        self.root = helper(self.root, val)
        return self.root
