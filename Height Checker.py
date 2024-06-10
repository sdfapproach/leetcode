# https://leetcode.com/problems/height-checker/?envType=daily-question&envId=2024-06-10
# Height Checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        count = 0
        
        sorted_heights = sorted(heights)

        for i, height in enumerate(sorted_heights):
            if height != heights[i]:
                count += 1

        return count