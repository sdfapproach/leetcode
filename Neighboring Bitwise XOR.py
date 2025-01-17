# https://leetcode.com/problems/neighboring-bitwise-xor/?envType=daily-question&envId=2025-01-17
# Neighboring Bitwise XOR

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        n = len(derived)

        original = [0] * n

        for i in range(1, n):
            original[i] = derived[i - 1] ^ original[i - 1]
        if original[-1] ^ original[0] == derived[-1]:
            return True

        original = [0] * n
        original[0] = 1

        for i in range(1, n):
            original[i] = derived[i - 1] ^ original[i - 1]
        if original[-1] ^ original[0] == derived[-1]:
            return True

        return False