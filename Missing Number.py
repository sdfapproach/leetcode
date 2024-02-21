# https://leetcode.com/problems/missing-number/?envType=daily-question&envId=2024-02-20
# Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()

        # for i, num in enumerate(nums):
        #     if i != num:
        #         return i

        # return len(nums)
        
        # iterator = enumerate(nums)

        # missing_number = next((i for i, num in iterator if i != num), len(nums))

        # return missing_number

        n = len(nums)
        total_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        missing_number = total_sum - actual_sum
        return missing_number