# https://leetcode.com/problems/make-the-string-great/?envType=daily-question&envId=2024-04-05
# Make The String Great

class Solution:
    def makeGood(self, s: str) -> str:
        
        # stack = []

        # for c in s:

        #     if len(stack) <= 0:
        #         stack.append(c)
        #     elif abs(ord(stack[-1]) - ord(c)) == 32:
        #         stack.pop()
        #     else:
        #         stack.append(c)
        
        # return "".join(stack)

        stack = []

        for c in s:
            if stack and abs(ord(stack[-1]) - ord(c)) == 32:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)