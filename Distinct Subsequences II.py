# https://leetcode.com/problems/distinct-subsequences-ii/?envType=daily-question&envId=2026-09-07
# Distinct Subsequences II

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        
        MOD = 10**9 + 7

        dp = 1

        last = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')

            new_dp = (2 * dp - last[idx]) % MOD

            last[idx] = dp
            dp = new_dp

        return (dp - 1) % MOD