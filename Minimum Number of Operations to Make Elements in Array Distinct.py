# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/?envType=daily-question&envId=2025-04-08
# Minimum Number of Operations to Make Elements in Array Distinct

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        count = 0
        
        for i in range(ceil(len(nums)/3)):

            arr = nums[i * 3 : ]

            if len(arr) == len(set(arr)):
                return count
            count += 1

        return count