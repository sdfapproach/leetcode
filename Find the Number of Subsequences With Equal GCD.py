# https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/?envType=daily-question&envId=2026-07-14
# Find the Number of Subsequences With Equal GCD

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        
        MOD = 10**9 + 7
        max_value = max(nums)

        dp = [[0] * (max_value + 1) for _ in range(max_value + 1)]
        dp[0][0] = 1

        for x in nums:
            new_dp = [row[:] for row in dp]

            for g1 in range(max_value + 1):
                for g2 in range(max_value + 1):
                    count = dp[g1][g2]

                    if count == 0:
                        continue

                    ng1 = gcd(g1, x)
                    new_dp[ng1][g2] = (
                        new_dp[ng1][g2] + count
                    ) % MOD

                    ng2 = gcd(g2, x)
                    new_dp[g1][ng2] = (
                        new_dp[g1][ng2] + count
                    ) % MOD

            dp = new_dp

        answer = 0

        for g in range(1, max_value + 1):
            answer = (answer + dp[g][g]) % MOD

        return answer