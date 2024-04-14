# https://leetcode.com/problems/sum-of-left-leaves/?envType=daily-question&envId=2024-04-14
# Sum of Left Leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def is_leaf(node):
            return node is not None and node.left is None and node.right is None

        def dfs(node):
            if not node:
                return 0
            
            sum_left = 0
            if node.left:
                if is_leaf(node.left):
                    sum_left += node.left.val
                else:
                    sum_left += dfs(node.left)
            
            if node.right:
                sum_left += dfs(node.right)
            
            return sum_left
        
        return dfs(root)