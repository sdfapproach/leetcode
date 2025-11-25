# https://leetcode.com/problems/smallest-integer-divisible-by-k/?envType=daily-question&envId=2025-11-25
# Smallest Integer Divisible by K

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainder = 1 % k 
        length = 1
        
        while length <= k:
            if remainder == 0:
                return length
            
            remainder = (remainder * 10 + 1) % k
            length += 1
            
        return -1