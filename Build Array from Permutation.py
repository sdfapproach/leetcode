# https://leetcode.com/problems/build-array-from-permutation/?envType=daily-question&envId=2025-05-06
# Build Array from Permutation

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        return [nums[num] for num in nums]