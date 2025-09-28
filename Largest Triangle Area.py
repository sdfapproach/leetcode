# https://leetcode.com/problems/largest-triangle-area/?envType=daily-question&envId=2025-09-27
# Largest Triangle Area

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        n = len(points)
        best = 0.0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    area2 = abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1))
                    if area2 > best * 2:
                        best = area2 / 2.0

        return best