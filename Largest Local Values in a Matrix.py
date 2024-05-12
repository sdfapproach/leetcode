# https://leetcode.com/problems/largest-local-values-in-a-matrix/?envType=daily-question&envId=2024-05-12
# Largest Local Values in a Matrix

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        size = len(grid) - 2

        new_grid = [[0] * size for _ in range(size)]

        for i in range(size):
            for j in range(size):

                # row1, row2, row3 = 0, 0, 0

                # row1 = max(grid[i][j], grid[i][j+1], grid[i][j+2])
                # row2 = max(grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2])
                # row3 = max(grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2])

                # new_grid[i][j] = max(row1, row2, row3)

                max_value = 0

                for di in range(3):
                    for dj in range(3):
                        max_value = max(max_value, grid[i + di][j + dj])

                new_grid[i][j] = max_value

        return new_grid