# https://leetcode.com/problems/remove-k-digits/?envType=daily-question&envId=2024-04-11
# Remove K Digits

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        final_stack = stack[:-k] if k else stack
        
        return ''.join(final_stack).lstrip('0') or '0'