# https://leetcode.com/problems/separate-squares-i/?envType=daily-question&envId=2026-01-13
# Separate Squares I

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        total_area = 0.0
        min_y = float('inf')
        max_y = float('-inf')

        for x, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)

        half = total_area / 2.0

        def area_below(h):
            area = 0.0
            for _, y, l in squares:
                if h <= y:
                    continue
                elif h >= y + l:
                    area += l * l
                else:
                    area += (h - y) * l
            return area

        left, right = min_y, max_y
        for _ in range(60):
            mid = (left + right) / 2
            if area_below(mid) < half:
                left = mid
            else:
                right = mid

        return left