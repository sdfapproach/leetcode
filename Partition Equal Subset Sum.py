# https://leetcode.com/problems/partition-equal-subset-sum/?envType=daily-question&envId=2025-04-07
# Partition Equal Subset Sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for t in range(target, num - 1, -1):
                dp[t] = dp[t] or dp[t - num]
        
        return dp[target]