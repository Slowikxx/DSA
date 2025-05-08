# Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree from left to right

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    q = deque()
    q.append(root)
    
    while q:
        qLen = len(q)
        level = []
        
        for i in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    
    return res

# Time complexity: O(n)
# Space complexity: O(n)