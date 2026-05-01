# https://leetcode.com/problems/rotate-function/?envType=daily-question&envId=2026-05-01
# Rotate Function

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        n = len(nums)
        total = sum(nums)
        
        F = sum(i * num for i, num in enumerate(nums))
        
        ans = F
        
        for k in range(1, n):
            F = F + total - n * nums[n - k]
            ans = max(ans, F)
        
        return ans