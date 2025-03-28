# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/?envType=daily-question&envId=2025-03-28
# Maximum Number of Points From Grid Queries

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        if self.size[xr] < self.size[yr]:
            xr, yr = yr, xr
        self.parent[yr] = xr
        self.size[xr] += self.size[yr]

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        
        m = len(grid)
        n = len(grid[0])
        total_cells = m * n
        
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort(key=lambda x: x[0])
        
        sorted_queries = sorted([(q, idx) for idx, q in enumerate(queries)], key=lambda x: x[0])
        res = [0] * len(queries)
        
        dsu = DSU(total_cells)
        open_cell = [[False] * n for _ in range(m)]
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        cell_ptr = 0
        for q, q_idx in sorted_queries:
            while cell_ptr < len(cells) and cells[cell_ptr][0] < q:
                val, i, j = cells[cell_ptr]
                open_cell[i][j] = True
                pos = i * n + j
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and open_cell[ni][nj]:
                        npos = ni * n + nj
                        dsu.union(pos, npos)
                cell_ptr += 1
            
            if open_cell[0][0]:
                res[q_idx] = dsu.size[dsu.find(0)]
            else:
                res[q_idx] = 0
        
        return res