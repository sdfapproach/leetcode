# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/?envType=daily-question&envId=2025-01-28
# Maximum Number of Fish in a Grid

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or visited[r][c] or grid[r][c] == 0:
                return 0
            
            visited[r][c] = True
            fish_count = grid[r][c]

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                fish_count += dfs(r + dr, c + dc)

            return fish_count

        max_fish = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and not visited[r][c]:
                    max_fish = max(max_fish, dfs(r, c))

        return max_fish