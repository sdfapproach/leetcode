# https://leetcode.com/problems/magic-squares-in-grid/?envType=daily-question&envId=2024-08-09
# Magic Squares In Grid

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def is_magic(square):
            if sorted(square) != list(range(1, 10)):
                return False
            
            s1 = sum(square[0:3])
            s2 = sum(square[3:6])
            s3 = sum(square[6:9])
            s4 = sum(square[0::3])
            s5 = sum(square[1::3])
            s6 = sum(square[2::3])
            s7 = sum(square[0::4])
            s8 = sum(square[2:8:2])

            return s1 == s2 == s3 == s4 == s5 == s6 == s7 == s8 == 15

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        for i in range(rows - 2):
            for j in range(cols - 2):
                square = [
                    grid[i][j], grid[i][j+1], grid[i][j+2],
                    grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                    grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]
                ]
                
                if is_magic(square):
                    count += 1
                    
        return count