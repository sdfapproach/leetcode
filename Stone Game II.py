# https://leetcode.com/problems/stone-game-ii/?envType=daily-question&envId=2024-08-20
# Stone Game II

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)
    
        suffix_sums = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]
        
        dp = [[0] * (n + 1) for _ in range(n)]
        
        def dfs(i, m):
            if i >= n:
                return 0
            if dp[i][m] != 0:
                return dp[i][m]
            
            max_stones = 0

            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break
                max_stones = max(max_stones, suffix_sums[i] - dfs(i + x, max(m, x)))
            
            dp[i][m] = max_stones

            return max_stones
        
        return dfs(0, 1)