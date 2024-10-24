# https://leetcode.com/problems/cousins-in-binary-tree-ii/?envType=daily-question&envId=2024-10-23
# Cousins in Binary Tree II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        root.val = 0
        queue = deque([(root, root)])
        
        while queue:
            size = len(queue)
            level_nodes = []
            next_level_sum = 0
            
            for _ in range(size):
                node, parent = queue.popleft()
                
                children_sum = 0
                if node.left:
                    children_sum += node.left.val
                    queue.append((node.left, node))
                    next_level_sum += node.left.val
                if node.right:
                    children_sum += node.right.val
                    queue.append((node.right, node))
                    next_level_sum += node.right.val
                    
                level_nodes.append((node, parent, children_sum))
            
            for node, parent, children_sum in level_nodes:
                cousin_sum = next_level_sum - children_sum
                if node.left:
                    node.left.val = cousin_sum
                if node.right:
                    node.right.val = cousin_sum

        return root