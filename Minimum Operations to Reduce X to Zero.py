# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/?envType=daily-question&envId=2026-09-23
# Minimum Operations to Reduce X to Zero

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        
        target = sum(nums) - x

        if target < 0:
            return -1

        if target == 0:
            return len(nums)

        left = 0
        total = 0
        max_len = -1

        for right in range(len(nums)):
            total += nums[right]

            while total > target:
                total -= nums[left]
                left += 1

            if total == target:
                max_len = max(max_len, right - left + 1)

        if max_len == -1:
            return -1

        return len(nums) - max_len