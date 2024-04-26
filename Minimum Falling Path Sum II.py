# https://leetcode.com/problems/minimum-falling-path-sum-ii/?envType=daily-question&envId=2024-04-26
# Minimum Falling Path Sum II

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return min(grid[0])

        dp = [[float('inf')] * n for _ in range(n)]

        for j in range(n):
            dp[0][j] = grid[0][j]

        for i in range(1, n):
            for j in range(n):
                for k in range(n):
                    if j != k:
                        dp[i][j] = min(dp[i][j], dp[i-1][k] + grid[i][j])

        return min(dp[-1])