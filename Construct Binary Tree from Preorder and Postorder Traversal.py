# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/?envType=daily-question&envId=2025-02-23
# Construct Binary Tree from Preorder and Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return root
        
        left_root_val = preorder[1]
        L = postorder.index(left_root_val) + 1
        
        root.left = self.constructFromPrePost(preorder[1:1+L], postorder[:L])
        root.right = self.constructFromPrePost(preorder[1+L:], postorder[L:-1])
        
        return root
