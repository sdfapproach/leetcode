# https://leetcode.com/problems/rotate-string/?envType=daily-question&envId=2024-11-03
# Rotate String

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        for i in range(len(s)):

            if s == goal:
                return True

            s = s[1:] + s[0]

        return False