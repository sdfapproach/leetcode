# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/?envType=daily-question&envId=2026-08-11
# Smallest Missing Integer Greater Than Sequential Prefix Sum

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        
        prefix_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break

        seen = set(nums)

        x = prefix_sum
        while x in seen:
            x += 1

        return x