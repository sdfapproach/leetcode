# https://leetcode.com/problems/find-all-groups-of-farmland/?envType=daily-question&envId=2024-04-20
# Find All Groups of Farmland

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        results = []

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or land[r][c] == 0 or visited[r][c]:
                return (float('inf'), float('-inf'), float('inf'), float('-inf'))
            visited[r][c] = True
            top, bottom, left, right = r, r, c, c
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                tr, br, tl, rl = dfs(nr, nc)
                top = min(top, tr)
                bottom = max(bottom, br)
                left = min(left, tl)
                right = max(right, rl)
            return (top, bottom, left, right)
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 and not visited[i][j]:
                    top, bottom, left, right = dfs(i, j)
                    if top <= bottom and left <= right:
                        results.append([top, left, bottom, right])
        
        return results