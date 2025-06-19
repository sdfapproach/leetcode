# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/?envType=daily-question&envId=2025-06-19
# Partition Array Such That Maximum Difference Is K

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        count = 0
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]
            count += 1
            i += 1
            while i < n and nums[i] - start <= k:
                i += 1

        return count