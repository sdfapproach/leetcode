# https://leetcode.com/problems/path-with-maximum-gold/?envType=daily-question&envId=2024-05-14
# Path with Maximum Gold

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        max_gold = 0

        def dfs(x, y):

            gold_collected = grid[x][y]
            grid[x][y] = 0
            max_gold_here = 0
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                    max_gold_here = max(max_gold_here, dfs(nx, ny))
            grid[x][y] = gold_collected

            return gold_collected + max_gold_here

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    max_gold = max(max_gold, dfs(i, j))

        return max_gold
