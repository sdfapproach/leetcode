# https://leetcode.com/problems/find-largest-value-in-each-tree-row/?envType=daily-question&envId=2024-12-25
# Find Largest Value in Each Tree Row

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        largest = []
        
        def dfs(node, level = 0):

            if node:
                if len(largest) <= level:
                    largest.append(node.val)
                else:
                    largest[level] = max(largest[level], node.val)
                level += 1
                dfs(node.left, level)
                dfs(node.right, level)
        
        dfs(root)

        return largest