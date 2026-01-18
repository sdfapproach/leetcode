# https://leetcode.com/problems/largest-magic-square/?envType=daily-question&envId=2026-01-18
# Largest Magic Square

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        row_sum = [[0] * (n + 1) for _ in range(m)]
        col_sum = [[0] * (n) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                row_sum[i][j+1] = row_sum[i][j] + grid[i][j]
                col_sum[i+1][j] = col_sum[i][j] + grid[i][j]
        
        for k in range(min(m, n), 1, -1):
            
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    
                    if self.isMagic(grid, row_sum, col_sum, i, j, k):
                        return k
                        
        return 1

    def isMagic(self, grid, row_sum, col_sum, r, c, k):
        diag1 = 0
        diag2 = 0
        for x in range(k):
            diag1 += grid[r + x][c + x]
            diag2 += grid[r + x][c + k - 1 - x]
            
        if diag1 != diag2:
            return False
        
        target = diag1
        
        for x in range(k):
            rs = row_sum[r + x][c + k] - row_sum[r + x][c]
            if rs != target:
                return False
                
        for y in range(k):
            cs = col_sum[r + k][c + y] - col_sum[r][c + y]
            if cs != target:
                return False
                
        return True