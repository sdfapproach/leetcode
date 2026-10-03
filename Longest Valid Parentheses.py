# https://leetcode.com/problems/longest-valid-parentheses/?envType=daily-question&envId=2026-10-03
# Longest Valid Parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = [-1]
        answer = 0

        for i, ch in enumerate(s):

            if ch == '(':
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    answer = max(
                        answer,
                        i - stack[-1]
                    )

        return answer