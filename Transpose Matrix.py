# https://leetcode.com/problems/transpose-matrix/description/?envType=daily-question&envId=2023-12-10
# Transpose Matrix

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        col = len(matrix)
        row = len(matrix[0])

        new_matrix = [[None] * col for _ in range(row)]

        for i, vec in enumerate(matrix):
            for idx, num in enumerate(vec):
                new_matrix[idx][i] = num

        return new_matrix