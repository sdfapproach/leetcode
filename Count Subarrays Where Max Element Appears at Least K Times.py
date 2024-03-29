# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/?envType=daily-question&envId=2024-03-29
# Count Subarrays Where Max Element Appears at Least K Times

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        
        count = 0
        start = 0
        max_count = 0
        
        for end in range(len(nums)):
            if nums[end] == max_num:
                max_count += 1
            
            while max_count >= k:
                count += len(nums) - end
                
                if nums[start] == max_num:
                    max_count -= 1
                
                start += 1
        
        return count