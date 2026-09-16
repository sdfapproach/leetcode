# https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/?envType=daily-question&envId=2026-09-16
# Number of Sets of K Non-Overlapping Line Segments

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        
        MOD = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1

        for j in range(1, k + 1):
            prefix = 0

            for i in range(1, n):
                prefix = (
                    prefix + dp[i - 1][j - 1]
                ) % MOD

                dp[i][j] = (
                    dp[i - 1][j] + prefix
                ) % MOD

        return dp[n - 1][k]