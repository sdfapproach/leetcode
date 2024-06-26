# https://leetcode.com/problems/balance-a-binary-search-tree/?envType=daily-question&envId=2024-06-26
# Balance a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inorder_traversal(root):

            if root is None:
                return []

            return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

        def sorted_array_to_bst(nums):

            if not nums:
                return None
            
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = sorted_array_to_bst(nums[:mid])
            root.right = sorted_array_to_bst(nums[mid+1:])
            
            return root

        nums = inorder_traversal(root)

        return sorted_array_to_bst(nums)
