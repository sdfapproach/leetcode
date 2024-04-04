# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/?envType=daily-question&envId=2024-04-04
# Maximum Nesting Depth of the Parentheses

class Solution:
    def maxDepth(self, s: str) -> int:
        
        count = 0
        maximum = 0

        for c in s:
            if c == "(":
                count += 1
                maximum = max(count, maximum)
            elif c == ")":
                count -= 1
            
        return maximum