# https://leetcode.com/problems/largest-divisible-subset/?envType=daily-question&envId=2025-04-06
# Largest Divisible Subset

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        
        dp = [1] * n
        
        prev = [-1] * n
        max_index = 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > dp[max_index]:
                max_index = i
        
        result = []
        i = max_index
        while i != -1:
            result.append(nums[i])
            i = prev[i]
        
        return result[::-1]