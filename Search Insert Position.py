# https://leetcode.com/problems/search-insert-position/description/
# Search Insert Position

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         for i, n in enumerate(nums):
#             if n >= target:
#                 return i

#         return len(nums)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = nums[mid]

            if mid_value == target:
                return mid
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return left