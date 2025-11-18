# https://leetcode.com/problems/1-bit-and-2-bit-characters/?envType=daily-question&envId=2025-11-18
# 1-bit and 2-bit Characters

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        i = 0
        n = len(bits)

        while i < n - 1:
            i += 1 if bits[i] == 0 else 2

        return i == n - 1