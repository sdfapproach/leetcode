# https://leetcode.com/problems/minimum-length-of-string-after-operations/?envType=daily-question&envId=2025-01-13
# Minimum Length of String After Operations

class Solution:
    def minimumLength(self, s: str) -> int:
        
        cnt = Counter(s)

        return sum(1 if x & 1 else 2 for x in cnt.values())