# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/?envType=daily-question&envId=2025-11-26
# Paths in Matrix Whose Sum Is Divisible by K

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        dp = [[[0] * k for _ in range(n)] for _ in range(m)]

        dp[0][0][grid[0][0] % k] = 1

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                
                for r in range(k):
                    
                    new_rem = (r + val) % k

                    if i > 0:
                        dp[i][j][new_rem] = (dp[i][j][new_rem] + dp[i-1][j][r]) % MOD
                    
                    if j > 0:
                        dp[i][j][new_rem] = (dp[i][j][new_rem] + dp[i][j-1][r]) % MOD

        return dp[m-1][n-1][0]