# https://leetcode.com/problems/largest-submatrix-with-rearrangements/?envType=daily-question&envId=2026-03-17
# Largest Submatrix With Rearrangements

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] += matrix[i-1][j]
        
        res = 0
        
        for i in range(m):
            row = sorted(matrix[i], reverse=True)
            
            for j in range(n):
                res = max(res, row[j] * (j + 1))
        
        return res