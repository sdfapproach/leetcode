# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/?envType=daily-question&envId=2025-06-12
# Maximum Difference Between Adjacent Elements in a Circular Array

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        
        diff = abs(nums[0] - nums[-1])

        for i in range(1, len(nums)):

            diff = max(diff, abs(nums[i] - nums[i-1]))

        return diff