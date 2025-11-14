# https://leetcode.com/problems/increment-submatrices-by-one/?envType=daily-question&envId=2025-11-14
# Increment Submatrices by One

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        mat = [[0] * (n + 1) for _ in range(n + 1)]

        for r1, c1, r2, c2 in queries:
            mat[r1][c1] += 1
            if c2 + 1 < n:
                mat[r1][c2 + 1] -= 1
            if r2 + 1 < n:
                mat[r2 + 1][c1] -= 1
            if r2 + 1 < n and c2 + 1 < n:
                mat[r2 + 1][c2 + 1] += 1

        for i in range(n):
            for j in range(1, n):
                mat[i][j] += mat[i][j - 1]

        for j in range(n):
            for i in range(1, n):
                mat[i][j] += mat[i - 1][j]

        return [row[:n] for row in mat[:n]]