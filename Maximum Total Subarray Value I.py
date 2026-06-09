# https://leetcode.com/problems/maximum-total-subarray-value-i/?envType=daily-question&envId=2026-06-09
# Maximum Total Subarray Value I

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        
        return (max(nums) - min(nums)) * k