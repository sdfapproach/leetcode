# https://leetcode.com/problems/trionic-array-i/?envType=daily-question&envId=2026-02-03
# Trionic Array I

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        
        n = len(nums)

        if n < 4:
            return False

        i = 0

        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0:
            return False

        start = i

        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        if i == start:
            return False

        start = i

        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        if i == start:
            return False 

        return i == n - 1
