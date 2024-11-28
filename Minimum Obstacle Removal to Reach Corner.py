# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/?envType=daily-question&envId=2024-11-28
# Minimum Obstacle Removal to Reach Corner

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        heap = [(0, 0, 0)]
        visited = [[False] * n for _ in range(m)]
        
        while heap:
            obstacles, x, y = heappop(heap)
            
            if x == m - 1 and y == n - 1:
                return obstacles
            
            if visited[x][y]:
                continue
            visited[x][y] = True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    heappush(heap, (obstacles + grid[nx][ny], nx, ny))
        
        return -1