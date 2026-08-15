# https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/?envType=daily-question&envId=2026-08-15
# Longest Subsequence With Non-Zero Bitwise XOR

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        
        total_xor = 0

        for x in nums:
            total_xor ^= x

        if total_xor != 0:
            return len(nums)

        if any(x != 0 for x in nums):
            return len(nums) - 1

        return 0