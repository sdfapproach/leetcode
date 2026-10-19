# https://leetcode.com/problems/find-target-indices-after-sorting-array/?envType=daily-question&envId=2026-10-19
# Find Target Indices After Sorting Array

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:

        return [i for i, num in enumerate(sorted(nums)) if num == target]