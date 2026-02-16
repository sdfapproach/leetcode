# https://leetcode.com/problems/reverse-bits/?envType=daily-question&envId=2026-02-16
# Reverse Bits

class Solution:
    def reverseBits(self, n: int) -> int:

        bit = str(bin(n))[2:]

        bit = ((32 - len(bit)) * "0") + bit

        return int(bit[::-1], 2)