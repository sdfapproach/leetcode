# https://leetcode.com/problems/trapping-rain-water/?envType=daily-question&envId=2024-04-12
# Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:``
        if not height:
            return 0

        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        waterTrapped = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    waterTrapped += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    waterTrapped += rightMax - height[right]
                right -= 1

        return waterTrapped