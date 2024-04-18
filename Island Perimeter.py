# https://leetcode.com/problems/island-perimeter/?envType=daily-question&envId=2024-04-18
# Island Perimeter

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        perimeter = 0

        for i, col in enumerate(grid):
            for j in range(len(col)):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2

        return perimeter