# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/?envType=daily-question&envId=2024-02-15
# Find Polygon With the Largest Perimeter

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        for i, num in enumerate(nums):
            if num < sum(nums[i:]) - num:
                return sum(nums[i:])

        return -1