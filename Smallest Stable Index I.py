# https://leetcode.com/problems/smallest-stable-index-i/?envType=daily-question&envId=2026-09-04
# Smallest Stable Index I

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        n = len(nums)

        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        prefix_max = nums[0]

        for i in range(n):
            prefix_max = max(prefix_max, nums[i])

            if prefix_max - suffix_min[i] <= k:
                return i

        return -1