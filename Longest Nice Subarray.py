# https://leetcode.com/problems/longest-nice-subarray/?envType=daily-question&envId=2025-03-18
# Longest Nice Subarray

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        l = 0
        mask = 0
        ans = 0
        
        for r in range(n):
            while mask & nums[r]:
                mask &= ~nums[l]
                l += 1
            mask |= nums[r]
            ans = max(ans, r - l + 1)
        
        return ans