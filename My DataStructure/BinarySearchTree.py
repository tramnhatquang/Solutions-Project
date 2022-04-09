from typing import List


class BSTNode:
    """
    A class represents the attributes of a node in a BST(Binary Search Tree)
    """
    def __init__(self, val=None, left=None, right=None):
        """
        Overloading constructor initializes the given value, leftNode, and
        rightNode
        :param val:
        :param left:
        :param right:
        """
        self.val = val
        self.left = left
        self.right = right


def iterative_insert(root: BSTNode, val: int) -> BSTNode:
    """
    Insert a value iteratively into a BST (no duplicate)
    :param root:  the given root of the BST
    :param val: the inserted value
    :return: the reference to the root of the BST
    """
    new_node = BSTNode(val)
    if not root:
        return new_node
    parent, curr = None, root
    while curr:
        parent = curr
        if curr.val < val:
            curr = curr.right
        elif curr.val > val:
            curr = curr.left
        else:  # curr.val == val
            print(f'{val} is already inserted')
    if parent.val < val:
        parent.right = new_node
    else:
        parent.left = new_node
    return root


def recursive_insert(root: BSTNode, val: int) -> BSTNode:
    """
    Insert a value recursively into a BST (no duplicate)
    :param root:  the given root of the BST
    :param val: the inserted value
    :return: the reference to the root of the BST
    """
    if not root:  # root is None
        root = BSTNode(val)
        return root
    # root is valid below here
    if root.val == val:
        print(f'{val} is already inserted')
    elif root.val < val:
        root.right = recursive_insert(root.right, val)
    else:
        root.left = recursive_insert(root.left, val)
    return root

### All three recursive traversals
def recursive_in_order_traversal(root: BSTNode) -> List[int]:
    """
    Recursive In-order traversal of the BST (visit left subtree -> node
    itself -> right subtree)
    :param root: root of the BST
    :return: list of nodes' values in in-order traversal
    """
    # One-liner Python approach
    # return [] if not root else recursive_in_order_traversal(root.left) + [
    #     root.val] + recursive_in_order_traversal(root.right)

    # Another approach (more details)
    res = []
    if root:
        res += recursive_in_order_traversal(root.left)
        res += [root.val]
        res += recursive_in_order_traversal(root.right)
    return res

def recursive_pre_order_traversal(root: BSTNode) -> List[int]:
    """
    Recursive pre-order traversal of the BST (visit node itself -> left
    subtree ->
    right subtree)
    :param root: root of the BST
    :return: list of nodes' values in pre-order traversal
    """
    # One-liner Python approach
    # return [] if not root else [root.val] + recursive_pre_order_traversal(
    #     root.left) + recursive_pre_order_traversal(root.right)

    # Another approach (more details)
    res = []
    if root:
        res += [root.val]
        res += recursive_pre_order_traversal(root.left)
        res += recursive_pre_order_traversal(root.right)
    return res

def recursive_post_order_traversal(root: BSTNode) -> List[int]:
    """
    Recursvie post-order traversal of the BST (visit left subtree -> right
    subtree ->
    node itself)
    :param root: root of the BST
    :return: list of nodes' values  in post-order traversal
    """
    # return [] if not root else recursive_post_order_traversal(root.left) + \
    #                            recursive_post_order_traversal(root.right) + [
    #                                root.val]
    # Another approach (more details)
    res = []
    if root:
        res += recursive_post_order_traversal(root.left)
        res += recursive_post_order_traversal(root.right)
        res += [root.val]
    return res

def recursive_traversal(root: BSTNode) -> None:
    """
    Returns the in-order, pre-order, and post-order traversals recursively in
    a BST
    :param root: the root of BST
    :return: None
    """
    print('In-order Traversal:', recursive_in_order_traversal(root))
    print('Pre-order Traversal:', recursive_pre_order_traversal(root))
    print('Post-order Traversal:', recursive_post_order_traversal(root))


### All three iterative traversals
def iterative_pre_order_traversal(root: BSTNode) -> List[int]:
    """
    Iterative pre-order traversal of the BST (visit left subtree -> right
    subtree ->
    node itself)
    :param root: root of the BST
    :return: list of nodes' values in pre-order traversal
    """
    stack, res = [root], []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return res

def iterative_in_order_traversal(root: BSTNode) -> List[int]:
    """
    Iterative in-order traversal of the BST (visit left subtree -> right
    subtree ->
    node itself)
    :param root: root of the BST
    :return: list of nodes' values in in-order traversal
    """
    stack, res =[], []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right

    return res


def iterative_post_order_traversal(root: BSTNode) -> List[int]:
    """
    Iterative post -order traversal of the BST (visit left subtree -> right
    subtree ->
    node itself)
    :param root: root of the BST
    :return: list of nodes' values in post-order traversal
    """
    ## This approach will visit each node twice
    ## Time: O(n) where n is the number of nodes in the BST
    ## Space: O(n)

    # traversal, stack = [], [(root, False)]
    # while stack:
    #     node, visited = stack.pop()
    #     if node:
    #         if visited:
    #             # add to result if visited
    #             traversal.append(node.val)
    #         else:
    #             # post-order
    #             stack.append((node, True))
    #             stack.append((node.right, False))
    #             stack.append((node.left, False))
    #
    # return traversal

    # The second approach is to modify the pre-order traversal and return the
    # inverse of the res array
    stack, res = [root], []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    return res[::-1]

def level_order_traversal(root: BSTNode) -> List[List[int]]:
    # The recursive way

    # levels = []
    #
    # def helper(node, level):
    #     if node:
    #         if len(levels) == level:
    #             levels.append([])
    #         levels[level] += [node.val]
    #         helper(node.left, level + 1)
    #         helper(node.right, level + 1)
    #
    # helper(root, 0)
    # return levels

    # The iterative way
    res, level = [], [root]
    while root and level:
        res.append([node.val for node in level])
        temp = []
        for node in level:
            temp.extend([node.left, node.right])
            print(list(temp))
        level = [leaf for leaf in temp if leaf]
        print(level)
        print()
    return res

def build_a_tree(lst: List[int]) -> BSTNode:
    """
    Construct a BST with a given list of nodes' values
    :param lst: the list of nodes' values that need to be inserted into BST
    :return: the reference to the root of BST
    """
    root = BSTNode(lst[0])
    for i in range(1, len(lst)):
        # root = iterative_insert(root, lst[i])
        root = recursive_insert(root, lst[i])
    return root

class BinarySeachTree:
    def __init__(self):
        self.root = None

    def insert(self, val):

        # Insert iteratively
        if not self.root:
            self.root = BSTNode(val)
            return self.root

        curr = self.root
        while True:
            if curr.val <= val:
                if not curr.right:
                    curr.right = BSTNode(val)
                    break
                else:
                    curr = curr.right
            else:
                if not curr.left:
                    curr.left = BSTNode(val)
                    break
                else:
                    curr = curr.left
        return self.root
