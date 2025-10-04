# https://leetcode.com/problems/container-with-most-water/?envType=daily-question&envId=2025-10-04
# Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1

        width = 0

        while left < right:

            vertical = 0

            if height[left] < height[right]:
                vertical = height[left]
                left += 1
            else:
                vertical = height[right]
                right -= 1

            width = max((vertical * (right - left + 1)), width)

        return width