# https://leetcode.com/problems/diameter-of-binary-tree/?envType=daily-question&envId=2024-02-27
# Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        def maxDepth(node):
            if not node:
                return 0
            left_depth = maxDepth(node.left)
            right_depth = maxDepth(node.right)

            self.diameter = max(self.diameter, left_depth + right_depth)

            return max(left_depth, right_depth) + 1

        maxDepth(root)
        return self.diameter