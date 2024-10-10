# https://leetcode.com/problems/maximum-width-ramp/?envType=daily-question&envId=2024-10-10
# Maximum Width Ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        # width = 0

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):

        #         if nums[i] <= nums[j]:
        #             width = max(width , j - i)
        
        # return width

        stack = []
        max_width = 0

        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                max_width = max(max_width, j - stack.pop())

        return max_width