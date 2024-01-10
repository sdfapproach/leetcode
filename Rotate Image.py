# https://leetcode.com/problems/rotate-image/
# Rotate Image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new_matrix = []

        for i in range(len(matrix)):
            new_list = []
            for j in range(len(matrix)):
                j = len(matrix) - j -1
                new_list.append(matrix[j][i])

            new_matrix.append(new_list)

        for i in range(len(matrix)):
            matrix[i] = new_matrix[i]