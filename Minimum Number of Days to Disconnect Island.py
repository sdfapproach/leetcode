# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/?envType=daily-question&envId=2024-08-11
# Minimum Number of Days to Disconnect Island

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        
        def is_connected(grid):
            def dfs(x, y):
                if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                    return
                grid[x][y] = 0
                for dx, dy in directions:
                    dfs(x + dx, y + dy)

            m, n = len(grid), len(grid[0])
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            land_count = sum(sum(row) for row in grid)

            if land_count == 0:
                return False

            found_island = False
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        if found_island:
                            return False
                        found_island = True
                        dfs(i, j)

            return found_island

        if not is_connected([row[:] for row in grid]):
            return 0

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if not is_connected([row[:] for row in grid]):
                        return 1
                    grid[i][j] = 1

        return 2