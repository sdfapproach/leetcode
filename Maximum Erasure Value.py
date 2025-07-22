# https://leetcode.com/problems/maximum-erasure-value/?envType=daily-question&envId=2025-07-22
# Maximum Erasure Value

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        last_index = {}
        left = 0
        curr_sum = 0
        max_sum = 0
        
        for right, v in enumerate(nums):
            if v in last_index and last_index[v] >= left:
                new_left = last_index[v] + 1
                for i in range(left, new_left):
                    curr_sum -= nums[i]
                left = new_left
            
            curr_sum += v
            last_index[v] = right
            
            if curr_sum > max_sum:
                max_sum = curr_sum
        
        return max_sum