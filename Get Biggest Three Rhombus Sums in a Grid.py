# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/?envType=daily-question&envId=2026-03-16
# Get Biggest Three Rhombus Sums in a Grid

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        
        m, n = len(grid), len(grid[0])
        vals = set()

        for r in range(m):
            for c in range(n):
                vals.add(grid[r][c])

                k = 1
                while r - k >= 0 and r + k < m and c - k >= 0 and c + k < n:
                    total = 0

                    for t in range(k):
                        total += grid[r - k + t][c + t]

                    for t in range(k):
                        total += grid[r + t][c + k - t]

                    for t in range(k):
                        total += grid[r + k - t][c - t]

                    for t in range(k):
                        total += grid[r - t][c - k + t]

                    vals.add(total)
                    k += 1

        return sorted(vals, reverse=True)[:3]