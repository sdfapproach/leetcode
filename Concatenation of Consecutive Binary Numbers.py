# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/?envType=daily-question&envId=2026-02-28
# Concatenation of Consecutive Binary Numbers

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        MOD = 10**9 + 7
        ans = 0
        bitlen = 0

        for i in range(1, n + 1):
            if (i & (i - 1)) == 0:
                bitlen += 1

            ans = ((ans << bitlen) + i) % MOD

        return ans