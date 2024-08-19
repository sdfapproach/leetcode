# https://leetcode.com/problems/2-keys-keyboard/?envType=daily-question&envId=2024-08-19
# 2 Keys Keyboard

class Solution:
    def minSteps(self, n: int) -> int:
        
        dp = [0] * (n + 1)
    
        for i in range(2, n + 1):
            dp[i] = i 
            for j in range(i - 1, 1, -1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i // j))
        
        return dp[n]