# https://leetcode.com/problems/n-ary-tree-postorder-traversal/?envType=daily-question&envId=2024-08-26
# N-ary Tree Postorder Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        def helper(node):
            if node:
                for child in node.children:
                    helper(child)
                result.append(node.val)
        
        result = []
        helper(root)

        return result