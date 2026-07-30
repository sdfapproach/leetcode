# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/?envType=daily-question&envId=2026-07-30
# Minimum Number of Pushes to Type Word I

class Solution:
    def minimumPushes(self, word: str) -> int:
        
        answer = 0

        for i in range(len(word)):
            answer += i // 8 + 1

        return answer