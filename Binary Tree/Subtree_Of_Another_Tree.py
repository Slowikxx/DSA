# Given the roots of two binary trees, root and subRoot, return truw if there is a subtree of root with the same structure and node values of subRoot and false otherwise
# A subtree of a binary tree is a tree that consists of a node in tree and all of this node's descendants. The tree could also be considered as a subtree of itself

from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not subRoot:
        return True
    if not root:
        return False
    
    if isSameTree(root, subRoot):
        return True
    
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def isSameTree(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
    if not s and not t:
        return True
    if s and t and s.val == t.val:
        return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)
    
    return False

# Time Complexity: O(m * n), where m is the number of nodes in root and n is the number of nodes in subRoot
# Space complexity: O(m + n), where m and n are the heights of the trees