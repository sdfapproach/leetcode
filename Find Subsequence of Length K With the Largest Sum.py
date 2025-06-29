# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/?envType=daily-question&envId=2025-06-28
# Find Subsequence of Length K With the Largest Sum

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        nums = [[i, num] for i, num in enumerate(nums)]

        return [num[1] for num in sorted(sorted(nums, reverse=True, key = lambda x : x[1])[:k], key = lambda x : x[0])]