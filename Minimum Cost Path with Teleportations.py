# https://leetcode.com/problems/minimum-cost-path-with-teleportations/?envType=daily-question&envId=2026-01-28
# Minimum Cost Path with Teleportations

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        
        m, n = len(grid), len(grid[0])
    
        dist = [[math.inf] * n for _ in range(m)]
        dist[0][0] = 0
        
        cells_by_val = {}
        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                if val not in cells_by_val:
                    cells_by_val[val] = []
                cells_by_val[val].append((r, c))
                
        sorted_vals = sorted(cells_by_val.keys(), reverse=True)
        
        def propagate(d):
            for r in range(m):
                for c in range(n):
                    val = grid[r][c]
                    if r > 0:
                        d[r][c] = min(d[r][c], d[r-1][c] + val)
                    if c > 0:
                        d[r][c] = min(d[r][c], d[r][c-1] + val)

        propagate(dist)
        
        for _ in range(k):
            prev_dist = [row[:] for row in dist]
            
            min_cost_so_far = math.inf
            
            for val in sorted_vals:
                group = cells_by_val[val]
                
                group_min = math.inf
                for r, c in group:
                    group_min = min(group_min, prev_dist[r][c])
                
                min_cost_so_far = min(min_cost_so_far, group_min)
                
                for r, c in group:
                    dist[r][c] = min(dist[r][c], min_cost_so_far)
            
            propagate(dist)
            
        return dist[m-1][n-1]