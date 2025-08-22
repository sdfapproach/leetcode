# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/?envType=daily-question&envId=2025-08-22
# Find the Minimum Area to Cover All Ones I

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0]) if grid else 0
        INF = 10**9
        min_r, max_r, min_c, max_c = INF, -1, INF, -1

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if r < min_r: min_r = r
                    if r > max_r: max_r = r
                    if c < min_c: min_c = c
                    if c > max_c: max_c = c

        if max_r == -1:  # no 1s
            return 0

        return (max_r - min_r + 1) * (max_c - min_c + 1)