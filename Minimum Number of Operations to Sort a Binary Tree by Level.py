# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/?envType=daily-question&envId=2024-12-23
# Minimum Number of Operations to Sort a Binary Tree by Level

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        def min_swaps(arr):
            n = len(arr)
            sorted_arr = sorted(arr)
            index_map = {v: i for i, v in enumerate(arr)}
            swaps = 0
            visited = [False] * n

            for i in range(n):
                if visited[i] or arr[i] == sorted_arr[i]:
                    continue
                
                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = index_map[sorted_arr[j]]
                    cycle_size += 1

                if cycle_size > 1:
                    swaps += cycle_size - 1
            
            return swaps

        queue = deque([root])
        total_swaps = 0
        
        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            total_swaps += min_swaps(current_level)

        return total_swaps