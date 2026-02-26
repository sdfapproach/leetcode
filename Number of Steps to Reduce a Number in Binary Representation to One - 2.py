# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/?envType=daily-question&envId=2026-02-26
# Number of Steps to Reduce a Number in Binary Representation to One

class Solution:
    def numSteps(self, s: str) -> int:
        
        steps = 0
        carry = 0
        
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i])
            
            if bit + carry == 1:
                steps += 2
                carry = 1
            else:
                steps += 1
        
        return steps + carry