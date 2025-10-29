# https://leetcode.com/problems/smallest-number-with-all-set-bits/?envType=daily-question&envId=2025-10-29
# Smallest Number With All Set Bits

class Solution:
    def smallestNumber(self, n: int) -> int:

        return int("1" * (len(str(bin(n)))-2), 2)