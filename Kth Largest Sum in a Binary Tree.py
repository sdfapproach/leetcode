# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/?envType=daily-question&envId=2024-10-22
# Kth Largest Sum in a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        level = [0]

        def dfs(node, depth = 0):

            if node:

                if len(level) <= depth:
                    level.append(node.val)
                else:
                    level[depth] += node.val

                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        dfs(root)

        level.sort(reverse=True)

        if len(level) >= k:
            return level[k-1]
        else:
            return -1