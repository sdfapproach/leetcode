# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/?envType=daily-question&envId=2024-05-02
# Largest Positive Integer That Exists With Its Negative

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        # nums = sorted(nums)

        # f, b = 0, len(nums) - 1

        # while f < b:

        #     if nums[f] < 0 and abs(nums[f]) == nums[b]:
        #         return nums[b]
        #     elif nums[f] < 0 and abs(nums[f]) > nums[b]:
        #         f += 1
        #     else:
        #         b -= 1

        # return -1

        num_set = set(nums)
        max_k = -1

        for num in nums:
            if -num in num_set and num > 0:
                max_k = max(max_k, num)

        return max_k if max_k != -1 else -1