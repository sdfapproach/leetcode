# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/?envType=daily-question&envId=2025-04-09
# Minimum Operations to Make Array Values Equal to K

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        if any(x < k for x in nums):
            return -1
        
        distinct_above_k = {x for x in nums if x > k}

        return len(distinct_above_k)