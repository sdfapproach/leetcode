# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/?envType=daily-question&envId=2026-07-02
# Find a Safe Walk Through a Grid

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        
        m, n = len(grid), len(grid[0])

        INF = float('inf')
        dist = [[INF] * n for _ in range(m)]

        dist[0][0] = grid[0][0]

        dq = deque([(0, 0)])

        while dq:
            x, y = dq.popleft()

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    cost = grid[nx][ny]
                    nd = dist[x][y] + cost

                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd

                        if cost == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))

        return dist[m - 1][n - 1] < health