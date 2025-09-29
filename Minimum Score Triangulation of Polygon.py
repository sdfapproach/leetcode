# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/?envType=daily-question&envId=2025-09-29
# Minimum Score Triangulation of Polygon

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        n = len(values)
        dp = [[0]*n for _ in range(n)]
        for length in range(2, n):  # gap = j - i
            for i in range(n - length):
                j = i + length
                best = float('inf')
                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + values[i]*values[k]*values[j]
                    if cost < best:
                        best = cost
                dp[i][j] = 0 if best == float('inf') else best
        return dp[0][n-1]