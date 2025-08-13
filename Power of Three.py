# https://leetcode.com/problems/power-of-three/?envType=daily-question&envId=2025-08-13
# Power of Three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n < 1:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1