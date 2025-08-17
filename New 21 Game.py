# https://leetcode.com/problems/new-21-game/?envType=daily-question&envId=2025-08-17
# New 21 Game

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window = 1.0
        ans = 0.0

        for i in range(1, n + 1):
            dp[i] = window / maxPts
            if i < k:
                window += dp[i]
            else:
                ans += dp[i]
            if i - maxPts >= 0:
                if i - maxPts < k:
                    window -= dp[i - maxPts]
        return ans