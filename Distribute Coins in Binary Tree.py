# https://leetcode.com/problems/distribute-coins-in-binary-tree/?envType=daily-question&envId=2024-05-18
# Distribute Coins in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            left_moves = dfs(node.left)
            right_moves = dfs(node.right)
            
            total_moves = abs(left_moves) + abs(right_moves)
            
            balance = node.val + left_moves + right_moves - 1
            
            nonlocal moves
            moves += total_moves
            
            return balance

        moves = 0
        dfs(root)
        return moves