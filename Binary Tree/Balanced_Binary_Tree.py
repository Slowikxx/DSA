# Given a binary tree return true if it is height-balanced
# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1

from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def isBalanced(root: Optional[TreeNode]) -> bool:
    
    def dfs(root : Optional[TreeNode]) -> [bool, int]:
        if not root: return [True, 0]
        
        left = dfs(root.left)
        right = dfs(root.right)
        
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        
        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]

# Time complexity: O(n)
# Space complexity: O(h)