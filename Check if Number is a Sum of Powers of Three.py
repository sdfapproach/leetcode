# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/?envType=daily-question&envId=2025-03-04
# Check if Number is a Sum of Powers of Three

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        ternary = ""
        while n:
            ternary = str(n % 3) + ternary
            n //= 3
        
        return '2' not in ternary