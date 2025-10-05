# https://leetcode.com/problems/pacific-atlantic-water-flow/?envType=daily-question&envId=2025-10-05
# Pacific Atlantic Water Flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])

        def bfs(starts):
            from collections import deque
            vis = [[False]*n for _ in range(m)]
            q = deque()
            for r, c in starts:
                vis[r][c] = True
                q.append((r, c))
            dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not vis[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        vis[nr][nc] = True
                        q.append((nr, nc))
            return vis

        pac_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        atl_starts = [(m-1, c) for c in range(n)] + [(r, n-1) for r in range(m)]

        pac = bfs(pac_starts)
        atl = bfs(atl_starts)

        res = [[r, c] for r in range(m) for c in range(n) if pac[r][c] and atl[r][c]]

        return res