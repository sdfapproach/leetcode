# https://leetcode.com/problems/construct-uniform-parity-array-ii/?envType=daily-question&envId=2026-09-03
# Construct Uniform Parity Array II

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        minimum = min(nums1)

        if minimum % 2 == 1:
            return True

        return all(x % 2 == 0 for x in nums1)