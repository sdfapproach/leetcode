# https://leetcode.com/problems/first-missing-positive/?envType=daily-question&envId=2024-03-26
# First Missing Positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
    
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                nums[val - 1] = -abs(nums[val - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1