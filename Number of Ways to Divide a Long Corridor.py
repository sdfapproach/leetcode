# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/?envType=daily-question&envId=2025-12-14
# Number of Ways to Divide a Long Corridor

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
        MOD = 10**9 + 7
        
        s_indices = [i for i, char in enumerate(corridor) if char == 'S']
        
        num_seats = len(s_indices)
        
        if num_seats == 0 or num_seats % 2 != 0:
            return 0
        
        ways = 1
        
        for i in range(1, num_seats - 1, 2):
            distance = s_indices[i + 1] - s_indices[i]
            
            ways = (ways * distance) % MOD
            
        return ways