# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/?envType=daily-question&envId=2025-04-04
# Lowest Common Ancestor of Deepest Leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return (None, 0)

            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)

            if left_depth > right_depth:
                return (left_node, left_depth + 1)
            elif right_depth > left_depth:
                return (right_node, right_depth + 1)
            else:
                return (node, left_depth + 1)
        
        lca, _ = dfs(root)
        return lca