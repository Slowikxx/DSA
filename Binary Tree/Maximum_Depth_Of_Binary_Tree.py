# Given the root of a binary tree return its depth
# Depth is defined as the number of nodes along the longest path from the root node down to the farthest leaf node

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

# Time complexity: O(n), where n is the number of nodes in the tree
# Space complexity: O(h), where h is the height of the tree, worst case O(n)

# Iterative approach using a queue (BFS)

def maxDepthBFS(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    level = 0
    q = deque([root])
    
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    
    return level

# Time complexity: O(n), where n is the number of nodes in the tree
# Space complexity: O(n)

# Iterative approach using a stack (DFS)

def maxDepthIDFS(root: Optional[TreeNode]) -> int:
    stack = [[root, 1]]
    res = 0
    
    while stack:
        node, depth = stack.pop()
        
        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    
    return res

# Time complexity: O(n), where n is the number of nodes in the tree
# Space complexity: O(n)