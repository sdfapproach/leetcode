# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/?envType=daily-question&envId=2025-02-26
# Maximum Absolute Sum of Any Subarray

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        mod = 10**9 + 7
        prefix = 0
        max_prefix = 0
        min_prefix = 0
        
        for num in nums:
            prefix += num
            max_prefix = max(max_prefix, prefix)
            min_prefix = min(min_prefix, prefix)
        
        return (max_prefix - min_prefix) % mod