# https://leetcode.com/problems/largest-perimeter-triangle/?envType=daily-question&envId=2025-09-28
# Largest Perimeter Triangle

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)

        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if a < b + c:
                return a + b + c

        return 0