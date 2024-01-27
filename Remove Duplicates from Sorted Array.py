# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # new_nums=[]

        # i = 0
        # while i < len(nums):
        #     if nums[i] in new_nums:
        #         nums.pop(i)
        #     else:
        #         new_nums.append(nums[i])
        #         i += 1
        
        # return len(nums)

        if not nums:
            return 0
        
        last_unique = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[last_unique]:
                last_unique += 1
                nums[last_unique] = nums[i]
        
        return last_unique + 1