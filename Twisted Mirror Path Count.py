# https://leetcode.com/problems/twisted-mirror-path-count/?envType=daily-question&envId=2026-10-31
# Twisted Mirror Path Count

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == m - 1 and j == n - 1:
                    continue

                right, down = dp[i][j]

                if i == 0 and j == 0:
                    move_right = 1
                    move_down = 1

                elif grid[i][j] == 1:
                    move_right = down
                    move_down = right

                else:
                    move_right = (right + down) % MOD
                    move_down = (right + down) % MOD

                if j + 1 < n:
                    dp[i][j + 1][0] = (
                        dp[i][j + 1][0] + move_right
                    ) % MOD

                if i + 1 < m:
                    dp[i + 1][j][1] = (
                        dp[i + 1][j][1] + move_down
                    ) % MOD

        return sum(dp[m - 1][n - 1]) % MOD