# https://leetcode.com/problems/maximum-difference-between-increasing-elements/?envType=daily-question&envId=2025-06-16
# Maximum Difference Between Increasing Elements

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        diff = -1

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                if nums[i] < nums[j]:
                    diff = max(diff, nums[j] - nums[i])

        return diff
