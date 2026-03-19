# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/?envType=daily-question&envId=2026-03-19
# Count Submatrices With Equal Frequency of X and Y

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        prefixX = [[0]*n for _ in range(m)]
        prefixY = [[0]*n for _ in range(m)]
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 'X':
                    prefixX[i][j] = 1
                elif grid[i][j] == 'Y':
                    prefixY[i][j] = 1
                
                if i > 0:
                    prefixX[i][j] += prefixX[i-1][j]
                    prefixY[i][j] += prefixY[i-1][j]
                
                if j > 0:
                    prefixX[i][j] += prefixX[i][j-1]
                    prefixY[i][j] += prefixY[i][j-1]
                
                if i > 0 and j > 0:
                    prefixX[i][j] -= prefixX[i-1][j-1]
                    prefixY[i][j] -= prefixY[i-1][j-1]
                
                if prefixX[i][j] == prefixY[i][j] and prefixX[i][j] > 0:
                    res += 1
        
        return res