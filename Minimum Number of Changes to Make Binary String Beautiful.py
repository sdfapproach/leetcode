# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/?envType=daily-question&envId=2024-11-05
# Minimum Number of Changes to Make Binary String Beautiful

class Solution:
    def minChanges(self, s: str) -> int:
        
        count = 0

        for i in range(len(s)//2):

            idx = i * 2

            if s[idx] != s[idx+1]:
                count += 1

        return count