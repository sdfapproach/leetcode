# https://leetcode.com/problems/construct-product-matrix/?envType=daily-question&envId=2026-03-24
# Construct Product Matrix

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        MOD = 12345
        n, m = len(grid), len(grid[0])
        
        flat = [num for row in grid for num in row]
        size = len(flat)
        
        res = [1] * size
        
        prefix = 1
        for i in range(size):
            res[i] = prefix
            prefix = (prefix * flat[i]) % MOD
        
        suffix = 1

        for i in range(size - 1, -1, -1):
            res[i] = (res[i] * suffix) % MOD
            suffix = (suffix * flat[i]) % MOD
        
        return [res[i*m:(i+1)*m] for i in range(n)]