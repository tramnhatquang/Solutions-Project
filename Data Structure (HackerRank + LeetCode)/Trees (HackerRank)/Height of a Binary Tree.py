# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    if not root:
        return -1

    left = height(root.left)
    right = height(root.right)
    return max(left, right) + 1
