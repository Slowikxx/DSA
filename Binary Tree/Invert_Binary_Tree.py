# You are given a root of a binary tree. Invert the binary tree and return its root


from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    temp = root.left
    root.left = root.right
    root.right = temp
    
    invertTree(root.left)
    invertTree(root.right)
    
    return root


# Time complexity: O(n), where n is the number of nodes in the tree
# Space complexity: O(n), for the recursion stack in the worst case (skewed tree)