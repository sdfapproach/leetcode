# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/?envType=daily-question&envId=2026-11-22
# Check if All A's Appears Before All B's

class Solution:
    def checkString(self, s: str) -> bool:
        
        window = ""

        for c in s:
            if window == "":
                window = c
            elif window == "b" and c == "a":
                return False
            elif window == "a" and c == "b":
                window = c

        return True
                