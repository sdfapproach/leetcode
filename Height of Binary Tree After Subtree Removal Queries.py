# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/?envType=daily-question&envId=2024-10-26
# Height of Binary Tree After Subtree Removal Queries

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        heights = defaultdict(int)
        
        sibling_heights = defaultdict(int)
        
        def calculate_height(node: TreeNode, depth: int = 0) -> int:
            if not node:
                return -1
            
            left_height = calculate_height(node.left, depth + 1)
            right_height = calculate_height(node.right, depth + 1)
            
            heights[node.val] = depth
            
            if node.left:
                sibling_heights[node.left.val] = right_height + 1
            if node.right:
                sibling_heights[node.right.val] = left_height + 1
                
            return max(left_height, right_height) + 1
        
        def find_max_height(node: TreeNode, curr_height: int, max_height: int) -> None:
            if not node:
                return
                
            heights[node.val] = max_height
            
            if node.left:
                new_height = max(curr_height + sibling_heights[node.left.val], max_height)
                find_max_height(node.left, curr_height + 1, new_height)
            
            if node.right:
                new_height = max(curr_height + sibling_heights[node.right.val], max_height)
                find_max_height(node.right, curr_height + 1, new_height)
        
        total_height = calculate_height(root)
        find_max_height(root, 0, 0)
        
        answer = []
        for query in queries:
            answer.append(heights[query])
            
        return answer