# https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/?envType=daily-question&envId=2025-12-10
# Count the Number of Computer Unlocking Permutations

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        
        MOD = 10**9 + 7
        n = len(complexity)
    
        root_complexity = complexity[0]
        
        for i in range(1, n):
            if complexity[i] <= root_complexity:
                return 0
                
        ans = 1

        for i in range(1, n):
            ans = (ans * i) % MOD
            
        return ans