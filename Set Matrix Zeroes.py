# https://leetcode.com/problems/set-matrix-zeroes/?envType=daily-question&envId=2025-05-21
# Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        x = []
        y = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == 0:
                    x.append(i)
                    y.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if i in x:
                    matrix[i][j] = 0
                if j in y:
                    matrix[i][j] = 0
        

