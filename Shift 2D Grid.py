# https://leetcode.com/problems/shift-2d-grid/?envType=daily-question&envId=2026-07-20
# Shift 2D Grid

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0])

        flatten = [value for row in grid for value in row]

        k %= m * n

        if k:
            flatten = flatten[-k:] + flatten[:-k]

        return [
            flatten[i * n:(i + 1) * n]
            for i in range(m)
        ]