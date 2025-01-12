# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/?envType=daily-question&envId=2025-01-12
# Check if a Parentheses String Can Be Valid

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        if len(s) % 2 != 0:
            return False

        min_open = 0
        max_open = 0

        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == '(':
                    min_open += 1
                    max_open += 1
                else:
                    min_open = max(min_open - 1, 0)
                    max_open -= 1
            else:
                min_open = max(min_open - 1, 0)
                max_open += 1

            if max_open < 0:
                return False

        return min_open == 0