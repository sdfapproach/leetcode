# https://leetcode.com/problems/spiral-matrix-iii/?envType=daily-question&envId=2024-08-08
# Spiral Matrix III

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
        r, c = rStart, cStart
        
        result = []
        
        total_cells = rows * cols
        
        step_size = 1
        
        dir_idx = 0
        
        while len(result) < total_cells:
            for _ in range(2):
                for _ in range(step_size):
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append((r, c))
                    r += directions[dir_idx][0]
                    c += directions[dir_idx][1]
                dir_idx = (dir_idx + 1) % 4
            
            step_size += 1
        
        return result