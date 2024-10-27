# https://leetcode.com/problems/count-square-submatrices-with-all-ones/?envType=daily-question&envId=2024-10-27
# Count Square Submatrices with All Ones

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    count += dp[i][j]

        return count