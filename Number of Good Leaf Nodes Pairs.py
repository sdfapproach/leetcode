# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/?envType=daily-question&envId=2024-07-18
# Number of Good Leaf Nodes Pairs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [0]

            left_depths = dfs(node.left)
            right_depths = dfs(node.right)

            for l in left_depths:
                for r in right_depths:
                    if l + r + 2 <= distance:
                        count[0] += 1

            return [d + 1 for d in left_depths + right_depths]

        count = [0]
        dfs(root)

        return count[0]