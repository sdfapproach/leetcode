# https://leetcode.com/problems/create-binary-tree-from-descriptions/?envType=daily-question&envId=2024-07-15
# Create Binary Tree From Descriptions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        nodes = {}
        children = set()
        
        for parent, child, isLeft in descriptions:

            if parent not in nodes:
                nodes[parent] = TreeNode(val=parent)
            if child not in nodes:
                nodes[child] = TreeNode(val=child)
            
            if isLeft == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            
            children.add(child)
        
        root = None

        for parent, _, _ in descriptions:

            if parent not in children:
                root = nodes[parent]
                break
        
        return root