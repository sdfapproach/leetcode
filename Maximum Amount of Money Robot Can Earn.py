# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/?envType=daily-question&envId=2026-04-02
# Maximum Amount of Money Robot Can Earn

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        
        m, n = len(coins), len(coins[0])
        
        dp = [[[float('-inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        dp[0][0][0] = coins[0][0]
        
        if coins[0][0] < 0:
            dp[0][0][1] = 0
        
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if dp[i][j][k] == float('-inf'):
                        continue
                    
                    for ni, nj in [(i+1, j), (i, j+1)]:
                        if ni >= m or nj >= n:
                            continue
                        
                        val = coins[ni][nj]
                        
                        dp[ni][nj][k] = max(
                            dp[ni][nj][k],
                            dp[i][j][k] + val
                        )
                        
                        if val < 0 and k < 2:
                            dp[ni][nj][k+1] = max(
                                dp[ni][nj][k+1],
                                dp[i][j][k]
                            )
        
        return max(dp[m-1][n-1])