# https://leetcode.com/problems/range-sum-of-bst/description/?envType=daily-question&envId=2024-01-08
# Range Sum of BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def preorder_traversal(root, sum=0):
            if root:
                if root.val >= low and root.val <= high:
                    sum += root.val
                sum = preorder_traversal(root.left, sum)
                sum = preorder_traversal(root.right, sum)
            return sum

        return preorder_traversal(root)