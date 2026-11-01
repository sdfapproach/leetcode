# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/?envType=daily-question&envId=2026-11-01
# Minimum Moves to Equal Array Elements

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        
        return sum(nums) - min(nums) * len(nums)