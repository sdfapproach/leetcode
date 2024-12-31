# https://leetcode.com/problems/count-ways-to-build-good-strings/?envType=daily-question&envId=2024-12-30
# Count Ways To Build Good Strings

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        MOD = 10**9 + 7

        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % MOD

        result = 0
        for i in range(low, high + 1):
            result = (result + dp[i]) % MOD

        return result