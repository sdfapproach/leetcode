# https://leetcode.com/problems/maximum-score-from-grid-operations/?envType=daily-question&envId=2026-04-29
# Maximum Score From Grid Operations

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        P = [[0] * (n + 1) for _ in range(n)]
        for c in range(n):
            for r in range(n):
                P[c][r+1] = P[c][r] + grid[r][c]
                
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            for j in range(n + 1):
                dp[i][j] = max(0, P[0][j] - P[0][i])
                
        for c in range(1, n):
            next_dp = [[0] * (n + 1) for _ in range(n + 1)]
            
            for i in range(n + 1):
                pref_max = [0] * (n + 1)
                curr_max = -1
                for j in range(n + 1):
                    if dp[j][i] > curr_max:
                        curr_max = dp[j][i]
                    pref_max[j] = curr_max
                    
                suff_max = [0] * (n + 1)
                curr_max = -1
                for j in range(n - 1, -1, -1):
                    k = j + 1
                    val = dp[k][i] + max(0, P[c][k] - P[c][i])
                    if val > curr_max:
                        curr_max = val
                    suff_max[j] = curr_max
                    
                for j in range(n + 1):
                    opt1 = pref_max[j] + max(0, P[c][j] - P[c][i])
                    opt2 = suff_max[j]
                    
                    next_dp[i][j] = max(opt1, opt2)
                    
            dp = next_dp
            
        return max(dp[i][0] for i in range(n + 1))