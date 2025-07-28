# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/?envType=daily-question&envId=2025-07-28
# Count Number of Maximum Bitwise-OR Subsets

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        target = 0
        for v in nums:
            target |= v
        
        dp = Counter()
        dp[0] = 1
        
        for v in nums:
            for or_val, cnt in list(dp.items()):
                dp[or_val | v] += cnt
        
        return dp[target]