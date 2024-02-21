# https://leetcode.com/problems/bitwise-and-of-numbers-range/?envType=daily-question&envId=2024-02-21
# Bitwise AND of Numbers Range

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        # bitwise_and = left

        # for i in range(left, right+1):
        #     if bitwise_and == 0:
        #         return 0

        #     bitwise_and = bitwise_and & i

        
        # return bitwise_and

        shift = 0

        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift