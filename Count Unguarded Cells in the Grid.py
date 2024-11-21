# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/?envType=daily-question&envId=2024-11-21
# Count Unguarded Cells in the Grid

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        g = [[0] * n for _ in range(m)]

        for i, j in guards:
            g[i][j] = 2
        for i, j in walls:
            g[i][j] = 2
        dirs = (-1, 0, 1, 0, -1)

        for i, j in guards:
            for a, b in pairwise(dirs):
                x, y = i, j
                while 0 <= x + a < m and 0 <= y + b < n and g[x + a][y + b] < 2:
                    x, y = x + a, y + b
                    g[x][y] = 1

        return sum(v == 0 for row in g for v in row)