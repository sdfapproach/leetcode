# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/?envType=daily-question&envId=2026-01-24
# Minimize Maximum Pair Sum in Array

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)
        ans = 0

        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n - 1 - i])

        return ans