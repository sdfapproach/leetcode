# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/?envType=daily-question&envId=2025-08-23
# Find the Minimum Area to Cover All Ones II

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0]) if m else 0
        if m == 0 or n == 0:
            return 0

        @lru_cache(maxsize=None)
        def min_area(si: int, ei: int, sj: int, ej: int) -> int:
            if si > ei or sj > ej:
                return 0
            x1 = math.inf
            y1 = math.inf
            x2 = -math.inf
            y2 = -math.inf
            for i in range(si, ei + 1):
                row = grid[i]
                for j in range(sj, ej + 1):
                    if row[j] == 1:
                        if i < x1: x1 = i
                        if j < y1: y1 = j
                        if i > x2: x2 = i
                        if j > y2: y2 = j
            return 0 if x1 is math.inf else (x2 - x1 + 1) * (y2 - y1 + 1)

        INF = 10**18
        ans = INF

        for i in range(m):
            top = min_area(0, i, 0, n - 1)
            for j in range(n):
                ans = min(ans,
                          top +
                          min_area(i + 1, m - 1, 0, j) +
                          min_area(i + 1, m - 1, j + 1, n - 1))

        for i in range(m):
            bottom = min_area(i, m - 1, 0, n - 1)
            for j in range(n):
                ans = min(ans,
                          bottom +
                          min_area(0, i - 1, 0, j) +
                          min_area(0, i - 1, j + 1, n - 1))

        for j in range(n):
            left = min_area(0, m - 1, 0, j)
            for i in range(m):
                ans = min(ans,
                          left +
                          min_area(0, i, j + 1, n - 1) +
                          min_area(i + 1, m - 1, j + 1, n - 1))

        for j in range(n):
            right = min_area(0, m - 1, j, n - 1)
            for i in range(m):
                ans = min(ans,
                          right +
                          min_area(0, i, 0, j - 1) +
                          min_area(i + 1, m - 1, 0, j - 1))

        for i1 in range(m):
            for i2 in range(i1 + 1, m):
                ans = min(ans,
                          min_area(0, i1, 0, n - 1) +
                          min_area(i1 + 1, i2, 0, n - 1) +
                          min_area(i2 + 1, m - 1, 0, n - 1))

        for j1 in range(n):
            for j2 in range(j1 + 1, n):
                ans = min(ans,
                          min_area(0, m - 1, 0, j1) +
                          min_area(0, m - 1, j1 + 1, j2) +
                          min_area(0, m - 1, j2 + 1, n - 1))

        return 0 if ans == INF else ans