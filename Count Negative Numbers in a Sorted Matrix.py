# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/?envType=daily-question&envId=2025-12-28
# Count Negative Numbers in a Sorted Matrix

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0

        for row in grid:
            for i, num in enumerate(row):
                if num < 0:
                    count += len(row) - i
                    break

        return count