# https://leetcode.com/problems/reverse-degree-of-a-string/?envType=daily-question&envId=2026-09-20
# Reverse Degree of a String

class Solution:
    def reverseDegree(self, s: str) -> int:

        ans = 0
        
        for i, c in enumerate(s):

            ans += (i + 1) * (123 - ord(c))
        
        return ans