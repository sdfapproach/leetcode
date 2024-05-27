# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/?envType=daily-question&envId=2024-05-27
# Special Array With X Elements Greater Than or Equal X

class Solution:
    def specialArray(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums)
        
        for i in range(n):
            x = n - i
            if nums[i] >= x and (i == 0 or nums[i-1] < x):
                return x
        
        return -1