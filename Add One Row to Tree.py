# https://leetcode.com/problems/add-one-row-to-tree/?envType=daily-question&envId=2024-04-16
# Add One Row to Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        def dfs(node, current_depth):
            if not node:
                return
            
            if current_depth == depth - 1:
                new_left = TreeNode(val)
                new_right = TreeNode(val)
                
                new_left.left = node.left
                new_right.right = node.right
                
                node.left = new_left
                node.right = new_right
            else:
                dfs(node.left, current_depth + 1)
                dfs(node.right, current_depth + 1)
        
        dfs(root, 1)
        return root