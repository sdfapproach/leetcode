# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/?envType=daily-question&envId=2026-01-03
# Number of Ways to Paint N × 3 Grid

class Solution:
    def numOfWays(self, n: int) -> int:
        
        MOD = 10**9 + 7
    
        if n == 1:
            return 12
            
        type_a = 6
        type_b = 6
        
        for _ in range(2, n + 1):
            new_type_a = (2 * type_a + 2 * type_b) % MOD
            new_type_b = (2 * type_a + 3 * type_b) % MOD
            
            type_a = new_type_a
            type_b = new_type_b
            
        return (type_a + type_b) % MOD