# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/?envType=daily-question&envId=2025-02-02
# Check if Array Is Sorted and Rotated

class Solution:
    def check(self, nums: List[int]) -> bool:
        
        n = len(nums)
        drop_count = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drop_count += 1

        return drop_count <= 1