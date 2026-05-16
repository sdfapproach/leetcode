# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/submissions/?envType=daily-question&envId=2026-05-16
# Find Minimum in Rotated Sorted Array II

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        
        return nums[left]