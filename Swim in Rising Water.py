# https://leetcode.com/problems/swim-in-rising-water/?envType=daily-question&envId=2025-10-06
# Swim in Rising Water

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]  # (cost, r, c)
        seen = [[False]*n for _ in range(n)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:
            cost, r, c = heapq.heappop(pq)
            if seen[r][c]:
                continue
            seen[r][c] = True
            if r == n-1 and c == n-1:
                return cost
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not seen[nr][nc]:
                    ncost = max(cost, grid[nr][nc])
                    heapq.heappush(pq, (ncost, nr, nc))