# https://leetcode.com/problems/balanced-binary-tree/?envType=daily-question&envId=2026-02-08
# Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return (True, 0)
            
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)
            
            if not left_balanced or not right_balanced:
                return (False, max(left_height, right_height) + 1)
            
            if abs(left_height - right_height) > 1:
                return (False, max(left_height, right_height) + 1)
            
            return (True, max(left_height, right_height) + 1)
        
        if root is None:
            return True
        
        balanced, _ = dfs(root)
        
        return balanced