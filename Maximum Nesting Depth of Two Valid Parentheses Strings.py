# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/?envType=daily-question&envId=2026-09-30
# Maximum Nesting Depth of Two Valid Parentheses Strings

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        
        answer = []
        depth = 0

        for ch in seq:
            if ch == '(':
                depth += 1
                answer.append(depth % 2)

            else:
                answer.append(depth % 2)
                depth -= 1

        return answer