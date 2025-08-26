# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/?envType=daily-question&envId=2025-08-26
# Maximum Area of Longest Diagonal Rectangle

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        
        best_d2 = -1
        best_area = 0

        for L, W in dimensions:
            d2 = L*L + W*W
            area = L*W
            
            if d2 > best_d2 or (d2 == best_d2 and area > best_area):
                best_d2 = d2
                best_area = area

        return best_area