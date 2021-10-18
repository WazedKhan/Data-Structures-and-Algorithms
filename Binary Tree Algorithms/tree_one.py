class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


a = Node('a')
b = Node('a')
c = Node('a')
d = Node('a')
e = Node('a')
f = Node('a')


a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


#       a
#      / \
#     b   c
#    / \   \
#   d   e   f

