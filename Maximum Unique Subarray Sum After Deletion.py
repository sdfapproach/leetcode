# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/description/?envType=daily-question&envId=2025-07-25
# Maximum Unique Subarray Sum After Deletion

class Solution:
    def maxSum(self, nums: List[int]) -> int:

        nums.sort()

        if nums[-1] <= 0:
            return nums[-1]
        else:
            return sum(set([num for num in nums if num > 0]))

        