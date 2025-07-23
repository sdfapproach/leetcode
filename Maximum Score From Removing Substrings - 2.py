# https://leetcode.com/problems/maximum-score-from-removing-substrings/?envType=daily-question&envId=2025-07-23
# Maximum Score From Removing Substrings

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        def remove_sub(s: str, sub0: str, sub1: str, pts: int):
            stack = []
            gain = 0
            for c in s:
                if stack and stack[-1] == sub0 and c == sub1:
                    stack.pop()
                    gain += pts
                else:
                    stack.append(c)
            return gain, "".join(stack)
        
        total = 0
        if x >= y:
            g, rem = remove_sub(s, 'a', 'b', x)
            total += g
            g2, _   = remove_sub(rem, 'b', 'a', y)
            total += g2
        else:
            g, rem = remove_sub(s, 'b', 'a', y)
            total += g
            g2, _   = remove_sub(rem, 'a', 'b', x)
            total += g2
        
        return total