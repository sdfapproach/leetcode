# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/?envType=daily-question&envId=2025-08-12
# Ways to Express an Integer as Sum of Powers

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        
        MOD = 10**9 + 7

        powers = []
        i = 1

        while True:
            p = i ** x
            if p > n: break
            powers.append(p)
            i += 1

        dp = [0] * (n + 1)
        dp[0] = 1

        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD

        return dp[n]