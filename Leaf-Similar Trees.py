# https://leetcode.com/problems/leaf-similar-trees/description/?envType=daily-question&envId=2024-01-09
# Leaf-Similar Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # list1 = []
        # list2 = []

        # def preorder_traversal(root, li):
        #     li = li
        #     if root:
        #         if root.left == None and root.right == None:
        #             li.append(root.val)
        #         preorder_traversal(root.left, li)
        #         preorder_traversal(root.right, li)

        # preorder_traversal(root1, list1)
        # preorder_traversal(root2, list2)

        # return list1 == list2
        
        def leaf_generator(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from leaf_generator(node.left)
                yield from leaf_generator(node.right)

        return list(leaf_generator(root1)) == list(leaf_generator(root2))