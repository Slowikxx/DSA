# Given the root of a non-empty binary tree, return the maximum path sum of a non-empty path.
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once.
# The path does not necessarily need to include the root.
# The path sum of a path is the sum of the node's values in the path.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def maxPathSum(root: Optional[TreeNode]) -> int:
    res = [root.val]
    
    def dfs(root):
        if not root:
            return 0
        
        leftMax = dfs(root.left)
        rightMax = dfs(root.right)
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)
        
        res[0] = max(res[0], root.val + rightMax + leftMax)
        
        return root.val + max(leftMax, rightMax)
    
    dfs(root)
    return res[0]

# Time complexity: O(n)
# Space complexity: O(n)