# https://leetcode.com/problems/number-of-ways-to-split-array/?envType=daily-question&envId=2025-01-03
# Number of Ways to Split Array

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        totalSum = sum(nums)
        prefixSum = 0
        count = 0
        
        for i in range(n - 1):
            prefixSum += nums[i]
            rightSum = totalSum - prefixSum
            if prefixSum >= rightSum:
                count += 1
                
        return count