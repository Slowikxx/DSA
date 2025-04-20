# Given the root of two binary trees, p and q, return true if trees are equivalent, otherwise return false
# Two binary trees are considered the same if they share the same exact structure and the nodes have the same values.

from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# Time complexity: O(n)
# Space complexity: O(n)