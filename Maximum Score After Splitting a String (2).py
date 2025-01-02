# https://leetcode.com/problems/maximum-score-after-splitting-a-string/?envType=daily-question&envId=2025-01-01
# Maximum Score After Splitting a String

class Solution:
    def maxScore(self, s: str) -> int:

        max_score = 0
        
        for i in range(1, len(s)):

            left = s[:i].count('0')
            right = s[i:].count('1')

            max_score = max(left+right, max_score)

        return max_score
