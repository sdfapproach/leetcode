# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/?envType=daily-question&envId=2026-08-30
# Removing Minimum and Maximum From Array

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        remove_front = right + 1

        remove_back = n - left

        remove_both = (left + 1) + (n - right)

        return min(
            remove_front,
            remove_back,
            remove_both
        )