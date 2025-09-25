# https://leetcode.com/problems/triangle/?envType=daily-question&envId=2025-09-25
# Triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        if not triangle:
            return 0
        dp = triangle[-1][:]
        for r in range(len(triangle) - 2, -1, -1):
            for c in range(len(triangle[r])):
                dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])
                
        return dp[0]