# https://leetcode.com/problems/binary-number-with-alternating-bits/?envType=daily-question&envId=2026-02-18
# Binary Number with Alternating Bits

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        bits = bin(n)[2:]
        
        for i in range(1, len(bits)):
            if bits[i-1] == bits[i]:
                return False

        return True