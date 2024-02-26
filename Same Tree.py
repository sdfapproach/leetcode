# https://leetcode.com/problems/same-tree/?envType=daily-question&envId=2024-02-26
# Same Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # def dfs(tree, result=None):
        #     if result is None:
        #         result = []
            
        #     if tree:
        #         result.append(tree.val)
        #         dfs(tree.left, result)
        #         dfs(tree.right, result)
        #     else:
        #         result.append(None)
        #         return result

        #     return result
        
        # return dfs(q) == dfs(p)

        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)