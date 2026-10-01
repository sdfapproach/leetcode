# https://leetcode.com/problems/valid-parentheses/?envType=daily-question&envId=2026-10-01
# Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in '({[':
                stack.append(ch)

            else:
                if not stack:
                    return False

                if stack.pop() != brackets[ch]:
                    return False

        return len(stack) == 0