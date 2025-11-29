# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/?envType=daily-question&envId=2025-11-29
# Minimum Operations to Make Array Sum Divisible by K

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        return sum(nums) % k