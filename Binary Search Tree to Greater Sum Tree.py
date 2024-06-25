# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/?envType=daily-question&envId=2024-06-25
# Binary Search Tree to Greater Sum Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def reverse_inorder(node, acc_sum):
            if not node:
                return acc_sum
            
            acc_sum = reverse_inorder(node.right, acc_sum)
            
            node.val += acc_sum
            
            acc_sum = node.val
            
            acc_sum = reverse_inorder(node.left, acc_sum)
            
            return acc_sum

        reverse_inorder(root, 0)

        return root