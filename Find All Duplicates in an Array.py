# https://leetcode.com/problems/find-all-duplicates-in-an-array/?envType=daily-question&envId=2024-03-25
# Find All Duplicates in an Array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        # nums.sort()

        # dup = []

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         dup.append(nums[i])

        # return dup

        duplicates = []

        for num in nums:
            index = abs(num) - 1

            if nums[index] < 0:
                duplicates.append(abs(num))
            else:
                nums[index] = -nums[index]

        return duplicates