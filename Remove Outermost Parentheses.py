# https://leetcode.com/problems/remove-outermost-parentheses/?envType=daily-question&envId=2026-10-08
# Remove Outermost Parentheses

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        answer = []
        depth = 0

        for ch in s:
            if ch == '(':
                if depth > 0:
                    answer.append(ch)
                depth += 1

            else:
                depth -= 1
                if depth > 0:
                    answer.append(ch)

        return ''.join(answer)