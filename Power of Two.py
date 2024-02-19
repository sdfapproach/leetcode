# https://leetcode.com/problems/power-of-two/description/?envType=daily-question&envId=2024-02-19
# Power of Two

import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 0:
            return False

        return n & (n-1) == 0

        # digit = len(str(n))

        # carry = math.ceil((digit-1)/3)

        # print(digit, carry)

        # if digit % 3 == 1:
        #     for i in range(4):
        #         if n == 2**((digit-1+carry)*3+i):
        #             return True
        # else: 
        #     for i in range(3):
        #         if n == 2**((digit-1+carry)*3+i):
        #             return True

        # return False