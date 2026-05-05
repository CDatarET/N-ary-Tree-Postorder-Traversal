"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def helper(self, root, arr):
        if not root:
            return

        for c in root.children:
            self.helper(c, arr)
        
        arr.append(root.val)

    def postorder(self, root):
        arr = []
        self.helper(root, arr)
        return arr
