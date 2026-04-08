# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/?envType=daily-question&envId=2026-04-08
# XOR After Range Multiplication Queries I

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        
        MOD = 10**9 + 7
        n = len(nums)
        
        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD
        
        res = 0

        for num in nums:
            res ^= num
        
        return res