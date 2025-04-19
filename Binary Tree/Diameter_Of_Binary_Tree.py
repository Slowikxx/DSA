# The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.
# The length of a path between two nodes in a binary tree is the number of edges between the nodes.
# Given the root of a binary tree return its diameter

from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    res = 0
    
    def dfs(curr: Optional[TreeNode]) -> int:
        nonlocal res
        if not curr:
            return 0
        
        left = dfs(curr.left)
        right = dfs(curr.right)
        
        res = max(res, left + right)
        
        return 1 + max(left,right)
        
    dfs(root)
    return res

# Time complexity: O(n), where n is the number of nodes in the tree
# Space complexity: O(h), where h is the height of the tree, which in the best case is balanced tree O(log n) and in the worst case is degenerate tree O(n)