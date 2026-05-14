# https://leetcode.com/problems/check-if-array-is-good/?envType=daily-question&envId=2026-05-14
# Check if Array is Good

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
        n = len(nums) - 1
        
        nums.sort()

        return nums == list(range(1, n + 1)) + [n]