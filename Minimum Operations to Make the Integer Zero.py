# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/?envType=daily-question&envId=2025-09-05
# Minimum Operations to Make the Integer Zero

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        
        if num1 == 0:
            return 0
        for k in range(1, 61):
            x = num1 - k * num2
            if x < k or x < 0:
                continue
            if x.bit_count() <= k:
                return k
        return -1