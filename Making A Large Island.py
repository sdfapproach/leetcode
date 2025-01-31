# https://leetcode.com/problems/making-a-large-island/?envType=daily-question&envId=2025-01-31
# Making A Large Island

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        island_id = 2
        island_sizes = {}
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, island_id):
            stack = [(r, c)]
            grid[r][c] = island_id
            size = 0
            while stack:
                x, y = stack.pop()
                size += 1
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = island_id
                        stack.append((nx, ny))
            return size

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[island_id] = dfs(r, c, island_id)
                    island_id += 1

        if not island_sizes:
            return 1

        max_island = max(island_sizes.values())

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    new_size = 1
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen.add(grid[nr][nc])
                    for id in seen:
                        new_size += island_sizes[id]
                    max_island = max(max_island, new_size)

        return max_island