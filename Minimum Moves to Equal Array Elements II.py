# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/?envType=daily-question&envId=2026-11-02
# Minimum Moves to Equal Array Elements II

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        
        nums.sort()
        median = nums[len(nums) // 2]

        return sum(abs(num - median) for num in nums)