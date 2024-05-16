# https://leetcode.com/problems/evaluate-boolean-binary-tree/?envType=daily-question&envId=2024-05-16
# Evaluate Boolean Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def evaluateTree(root):
            if not root:
                return False

            if not root.left and not root.right:
                return bool(root.val)

            left_value = evaluateTree(root.left)
            right_value = evaluateTree(root.right)

            if root.val == 2:
                return left_value or right_value
            elif root.val == 3:
                return left_value and right_value

        return evaluateTree(root)