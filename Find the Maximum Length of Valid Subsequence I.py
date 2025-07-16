# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/?envType=daily-question&envId=2025-07-16
# Find the Maximum Length of Valid Subsequence I

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        dp = [[0] * 2 for _ in range(2)]

        for x in nums:
            for y in range(2):
                dp[x % 2][y] = dp[y][x % 2] + 1

        return max(map(max, dp))