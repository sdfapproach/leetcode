# https://leetcode.com/problems/sort-colors/?envType=daily-question&envId=2025-05-17
# Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp