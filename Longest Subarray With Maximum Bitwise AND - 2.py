# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/?envType=daily-question&envId=2025-07-30
# Longest Subarray With Maximum Bitwise AND

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        mx = max(nums)
        best = cur = 0

        for v in nums:
            if v == mx:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0

        return best