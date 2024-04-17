# https://leetcode.com/problems/smallest-string-starting-from-leaf/?envType=daily-question&envId=2024-04-17
# Smallest String Starting From Leaf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        def dfs(node, path):
            if node is None:
                return
            
            path.append(chr(node.val + ord('a')))
            
            if not node.left and not node.right:
                current_str = ''.join(reversed(path))
                nonlocal smallest
                if smallest == "" or current_str < smallest:
                    smallest = current_str
            
            dfs(node.left, path)
            dfs(node.right, path)
            
            path.pop()

        smallest = ""
        dfs(root, [])
        return smallest