class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left


a = TreeNode('a')
b = TreeNode('b')
c = TreeNode('c')
d = TreeNode('d')
e = TreeNode('e')
f = TreeNode('f')

"""
        a
       / \
      b   c
     / \    \
    d   e    f
"""

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f