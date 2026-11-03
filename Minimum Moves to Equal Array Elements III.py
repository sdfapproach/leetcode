# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/?envType=daily-question&envId=2026-11-03
# Minimum Moves to Equal Array Elements III

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        return  (max(nums) * len(nums)) - sum(nums)