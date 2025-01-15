# https://leetcode.com/problems/minimize-xor/?envType=daily-question&envId=2025-01-15
# Minimize XOR

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        target_set_bits = bin(num2).count('1')
    
        x = 0
        for i in range(31, -1, -1):
            if target_set_bits == 0:
                break
            if num1 & (1 << i):
                x |= (1 << i)
                target_set_bits -= 1
        
        for i in range(32):
            if target_set_bits == 0:
                break
            if not (x & (1 << i)):
                x |= (1 << i)
                target_set_bits -= 1
        
        return x