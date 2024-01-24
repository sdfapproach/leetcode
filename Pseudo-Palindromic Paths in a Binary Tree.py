# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/?envType=daily-question&envId=2024-01-24
# Pseudo-Palindromic Paths in a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        def dfs(node, dic=None, pal=0):
            if dic is None:
                dic = {}

            if node:
                dic[node.val] = dic.get(node.val, 0) + 1

                if node.left is None and node.right is None:
                    odd = 0
                    for val in dic.values():
                        if val % 2 != 0:
                            odd += 1
                    if odd < 2:
                        pal += 1
                else:
                    if node.left:
                        pal = dfs(node.left, dic, pal)
                    if node.right:
                        pal = dfs(node.right, dic, pal)

                dic[node.val] -= 1
                if dic[node.val] == 0:
                    del dic[node.val]

            return pal

        return dfs(root)