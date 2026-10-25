# https://leetcode.com/problems/number-of-closed-islands/?envType=daily-question&envId=2026-10-25
# Number of Closed Islands

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            if grid[r][c] != 0:
                return

            grid[r][c] = 1

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(m):
            dfs(r, 0)
            dfs(r, n - 1)

        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c)

        answer = 0

        for r in range(1, m - 1):
            for c in range(1, n - 1):
                if grid[r][c] == 0:
                    answer += 1
                    dfs(r, c)

        return answer