# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/?envType=daily-question&envId=2026-01-22
# Minimum Pair Removal to Sort Array I

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        ops = 0
    
        while True:
            is_sorted = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    is_sorted = False
                    break
            
            if is_sorted:
                return ops
                
            min_sum = float('inf')
            merge_idx = -1
            
            for i in range(len(nums) - 1):
                curr_sum = nums[i] + nums[i+1]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    merge_idx = i
            
            new_val = nums[merge_idx] + nums[merge_idx+1]
            nums[merge_idx] = new_val
            nums.pop(merge_idx + 1)
            
            ops += 1