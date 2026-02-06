# https://leetcode.com/problems/minimum-removals-to-balance-array/?envType=daily-question&envId=2026-02-06
# Minimum Removals to Balance Array

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        n = len(nums)
        
        l = 0
        max_len = 1
        
        for r in range(n):
            while nums[r] > k * nums[l]:
                l += 1
            max_len = max(max_len, r - l + 1)
        
        return n - max_len