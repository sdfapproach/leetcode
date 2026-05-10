# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/submissions/1999903011/?envType=daily-question&envId=2026-05-10
# Maximum Number of Jumps to Reach the Last Index

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        dp = [-float('inf')] * n
        dp[0] = 0

        for i in range(n):
            if dp[i] == -float('inf'):
                continue

            for j in range(i + 1, n):
                if -target <= nums[j] - nums[i] <= target:
                    dp[j] = max(dp[j], dp[i] + 1)

        return dp[n - 1] if dp[n - 1] != -float('inf') else -1