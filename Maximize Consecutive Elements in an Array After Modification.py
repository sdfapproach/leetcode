# https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/?envType=daily-question&envId=2026-11-20
# Maximize Consecutive Elements in an Array After Modification

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        
        nums.sort()
        dp = defaultdict(int)

        for num in nums:
            dp[num + 1] = dp[num] + 1
            dp[num] = dp[num - 1] + 1

        return max(dp.values())