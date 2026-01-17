# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/?envType=daily-question&envId=2026-01-17
# Find the Largest Area of Square Inside Two Rectangles

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        
        n = len(bottomLeft)
        max_area = 0

        for i in range(n):
            a1, b1 = bottomLeft[i]
            c1, d1 = topRight[i]

            for j in range(i + 1, n):
                a2, b2 = bottomLeft[j]
                c2, d2 = topRight[j]

                x1 = max(a1, a2)
                y1 = max(b1, b2)
                x2 = min(c1, c2)
                y2 = min(d1, d2)

                width = x2 - x1
                height = y2 - y1

                if width > 0 and height > 0:
                    side = min(width, height)
                    max_area = max(max_area, side * side)

        return max_area