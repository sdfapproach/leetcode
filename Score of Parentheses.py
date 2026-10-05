# https://leetcode.com/problems/score-of-parentheses/?envType=daily-question&envId=2026-10-05
# Score of Parentheses

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        answer = 0
        depth = 0

        for i, ch in enumerate(s):
            if ch == '(':
                depth += 1

            else:
                depth -= 1

                if s[i - 1] == '(':
                    answer += 2 ** depth

        return answer