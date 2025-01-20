# https://leetcode.com/problems/first-completely-painted-row-or-column/?envType=daily-question&envId=2025-01-20
# First Completely Painted Row or Column

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        m, n = len(mat), len(mat[0])

        position = {}
        for i in range(m):
            for j in range(n):
                position[mat[i][j]] = (i, j)

        rows_painted = [0] * m
        cols_painted = [0] * n

        for i, value in enumerate(arr):
            r, c = position[value]
            rows_painted[r] += 1
            cols_painted[c] += 1

            if rows_painted[r] == n or cols_painted[c] == m:
                return i

        return -1