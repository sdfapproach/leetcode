# https://leetcode.com/problems/sort-matrix-by-diagonals/?envType=daily-question&envId=2025-08-28
# Sort Matrix by Diagonals

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)

        def sort_diag(si, sj, reverse):
            i, j = si, sj
            vals, cells = [], []
            while i < n and j < n:
                vals.append(grid[i][j])
                cells.append((i, j))
                i += 1; j += 1
            vals.sort(reverse=reverse)
            for (i, j), v in zip(cells, vals):
                grid[i][j] = v

        for i in range(n):
            sort_diag(i, 0, reverse=True)

        for j in range(1, n):
            sort_diag(0, j, reverse=False)

        return grid