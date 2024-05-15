# https://leetcode.com/problems/find-the-safest-path-in-a-grid/?envType=daily-question&envId=2024-05-15
# Find the Safest Path in a Grid

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        distance = [[float('inf')] * n for _ in range(n)]
        
        queue = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    distance[r][c] = 0
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and distance[nr][nc] == float('inf'):
                    distance[nr][nc] = distance[r][c] + 1
                    queue.append((nr, nc))
        
        left, right = 0, n

        def bfs_valid(safeness):
            if distance[0][0] < safeness or distance[n-1][n-1] < safeness:
                return False
            visited = [[False] * n for _ in range(n)]
            queue = deque([(0, 0)])
            visited[0][0] = True
            while queue:
                r, c = queue.popleft()
                if (r, c) == (n-1, n-1):
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and distance[nr][nc] >= safeness:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            return False
        
        while left < right:
            mid = (left + right + 1) // 2
            if bfs_valid(mid):
                left = mid
            else:
                right = mid - 1

        return left