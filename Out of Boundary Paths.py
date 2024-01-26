# https://leetcode.com/problems/out-of-boundary-paths/?envType=daily-question&envId=2024-01-26
# Out of Boundary Paths

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        dp = [[[0 for _ in range(maxMove + 1)] for _ in range(n)] for _ in range(m)]

        mod = 10**9 + 7

        for i in range(m):
            for k in range(1, maxMove + 1):
                dp[i][0][k] += 1
                dp[i][n-1][k] += 1

        for j in range(n):
            for k in range(1, maxMove + 1):
                dp[0][j][k] += 1
                dp[m-1][j][k] += 1

        for k in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    if i > 0:
                        dp[i][j][k] = (dp[i][j][k] + dp[i-1][j][k-1]) % mod
                    if i < m - 1:
                        dp[i][j][k] = (dp[i][j][k] + dp[i+1][j][k-1]) % mod
                    if j > 0:
                        dp[i][j][k] = (dp[i][j][k] + dp[i][j-1][k-1]) % mod
                    if j < n - 1:
                        dp[i][j][k] = (dp[i][j][k] + dp[i][j+1][k-1]) % mod

        return dp[startRow][startColumn][maxMove]