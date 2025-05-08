# Given a binary search tree (BST) where all node values are unique and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes
# The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that poth p and q as descendants.
# The ancestor is allowed to be a descendant of itself

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    cur = root
    
    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur

# Time complexity: O(logn) where n is the height of the tree
# Space complexity: O(1)