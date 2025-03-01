# https://leetcode.com/problems/apply-operations-to-an-array/?envType=daily-question&envId=2025-03-01
# Apply Operations to an Array

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        
        for i in range(len(nums)-1):

            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0

        new_nums = []

        zero = 0

        for num in nums:
            if num != 0:
                new_nums.append(num)
            else:
                zero += 1
            

        return new_nums + [0] * zero