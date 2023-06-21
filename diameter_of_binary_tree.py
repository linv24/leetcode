# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Ix 1 of the returned tuple is the maximum diameter computed at
        # any of the nodes in the tree, which may or may not contain
        # the root 
        return self.depth(root)[1]

    def depth(self, root: Optional[TreeNode]) -> int:
        # For each node, compute the maximum depth at the node, and track
        # the max diameter so far as well. Return both as a tuple
        l_dist, l_max = self.depth(root.left) if root.left else (0, 0)
        r_dist, r_max = self.depth(root.right) if root.right else (0, 0)
        return 1 + max(l_dist, r_dist), max(l_max, r_max, l_dist + r_dist)
