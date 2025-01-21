# https://leetcode.com/problems/grid-game/?envType=daily-question&envId=2025-01-21
# Grid Game

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        n = len(grid[0])
    
        top_prefix = [0] * n
        bottom_prefix = [0] * n

        top_prefix[0] = grid[0][0]

        for i in range(1, n):
            top_prefix[i] = top_prefix[i - 1] + grid[0][i]

        bottom_prefix[0] = grid[1][0]

        for i in range(1, n):
            bottom_prefix[i] = bottom_prefix[i - 1] + grid[1][i]

        min_points_left = float('inf')

        for i in range(n):
            top_remaining = top_prefix[n - 1] - top_prefix[i]
            bottom_remaining = bottom_prefix[i - 1] if i > 0 else 0
            min_points_left = min(min_points_left, max(top_remaining, bottom_remaining))

        return min_points_left