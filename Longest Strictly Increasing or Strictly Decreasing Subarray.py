# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/?envType=daily-question&envId=2025-02-03
# Longest Strictly Increasing or Strictly Decreasing Subarray

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        inc = 1
        dec = 1
        ans = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
            else:
                inc = 1
            
            if nums[i] < nums[i - 1]:
                dec += 1
            else:
                dec = 1
            
            ans = max(ans, inc, dec)

        return ans