# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/?envType=daily-question&envId=2026-04-12
# Minimum Distance to Type a Word Using Two Fingers

class Solution:
    def minimumDistance(self, word: str) -> int:
        
        def get_dist(c1, c2):
            if c1 == 26:
                return 0
            return abs(c1 // 6 - c2 // 6) + abs(c1 % 6 - c2 % 6)

        memo = {}

        def dp(i, f1, f2):
            if i == len(word):
                return 0
            if (i, f1, f2) in memo:
                return memo[(i, f1, f2)]
            
            target = ord(word[i]) - 65
            
            cost1 = get_dist(f1, target) + dp(i + 1, target, f2)
            cost2 = get_dist(f2, target) + dp(i + 1, f1, target)
            
            memo[(i, f1, f2)] = min(cost1, cost2)
            return memo[(i, f1, f2)]

        return dp(0, 26, 26)