# https://leetcode.com/problems/maximum-number-of-points-with-cost/?envType=daily-question&envId=2024-08-17
# Maximum Number of Points with Cost

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        m, n = len(points), len(points[0])
        
        dp = points[0]
        
        for i in range(1, m):
            new_dp = [0] * n
            
            left_max = [0] * n
            left_max[0] = dp[0]

            for j in range(1, n):
                left_max[j] = max(left_max[j-1] - 1, dp[j])
            
            right_max = [0] * n
            right_max[n-1] = dp[n-1]

            for j in range(n-2, -1, -1):
                right_max[j] = max(right_max[j+1] - 1, dp[j])
            
            for j in range(n):
                new_dp[j] = points[i][j] + max(left_max[j], right_max[j])
            
            dp = new_dp
        
        return max(dp)