# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=daily-question&envId=2025-08-24
# Longest Subarray of 1's After Deleting One Element

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        l = 0
        zeros = 0
        ans = 0

        for r, v in enumerate(nums):
            if v == 0:
                zeros += 1
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            ans = max(ans, r - l)

        return ans