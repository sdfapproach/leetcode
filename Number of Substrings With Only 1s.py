# https://leetcode.com/problems/number-of-substrings-with-only-1s/?envType=daily-question&envId=2025-11-16
# Number of Substrings With Only 1s

class Solution:
    def numSub(self, s: str) -> int:
        
        MOD = 10**9 + 7
        count = 0
        
        for sub in s.split("0"):
            if sub:
                leng = len(sub)
                count = (count + leng * (leng + 1) // 2) % MOD
        
        return count