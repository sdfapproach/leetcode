# https://leetcode.com/problems/lucky-numbers-in-a-matrix/?envType=daily-question&envId=2024-07-19
# Lucky Numbers in a Matrix

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        min_row = set([min(row) for row in matrix])

        max_col = set([max(row[j] for row in matrix) for j in range(len(matrix[0]))])

        return list(min_row & max_col)