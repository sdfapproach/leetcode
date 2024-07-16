# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/?envType=daily-question&envId=2024-07-16
# Step-By-Step Directions From a Binary Tree Node to Another

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def findPath(root, target, path):
            if root is None:
                return False
            if root.val == target:
                return True

            path.append('L')
            if findPath(root.left, target, path):
                return True
            path.pop()

            path.append('R')
            if findPath(root.right, target, path):
                return True
            path.pop()

            return False

        startPath = []
        destPath = []

        findPath(root, startValue, startPath)
        findPath(root, destValue, destPath)

        i = 0
        while i < len(startPath) and i < len(destPath) and startPath[i] == destPath[i]:
            i += 1

        steps = ['U'] * (len(startPath) - i)
        steps += destPath[i:]

        return ''.join(steps)