# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/?envType=daily-question&envId=2024-10-09
# Minimum Add to Make Parentheses Valid

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        top = -1

        for c in s:

            if c == "(":
                stack.append(c)
                top += 1
            elif c == ")":
                if top > -1 and stack[top] == "(":
                    stack.pop()
                    top -= 1
                else:
                    stack.append(c)
                    top += 1

        return len(stack)