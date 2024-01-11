# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/?envType=daily-question&envId=2024-01-11
# Maximum Difference Between Node and Ancestor

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def preorder_traversal(root, ancestor = [], max=0):

            if root:
                for n in ancestor:
                    num = abs(n - root.val)
                    if num > max:
                        max = num
               
                new_ancestor = ancestor + [root.val]

                max = preorder_traversal(root.left, new_ancestor, max)
                max = preorder_traversal(root.right, new_ancestor, max)
            
            return max

        return preorder_traversal(root)