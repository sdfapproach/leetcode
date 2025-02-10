# https://leetcode.com/problems/clear-digits/?envType=daily-question&envId=2025-02-10
# Clear Digits

class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = []

        for ch in s:
            if ch.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        
        return "".join(stack)
