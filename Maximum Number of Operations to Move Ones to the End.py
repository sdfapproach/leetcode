# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/?envType=daily-question&envId=2025-11-13
# Maximum Number of Operations to Move Ones to the End

class Solution:
    def maxOperations(self, s: str) -> int:
        
        ans = 0
        ones = 0

        for i, c in enumerate(s):
            if c == '1':
                ones += 1
            elif i + 1 == len(s) or s[i + 1] == '1':
                ans += ones

        return ans