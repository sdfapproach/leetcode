# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/?envType=daily-question&envId=2025-04-28
# Count Subarrays With Score Less Than K

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        left = 0
        curr_sum = 0
        count = 0
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while (curr_sum * (right - left + 1)) >= k:
                curr_sum -= nums[left]
                left += 1
            
            count += (right - left + 1)
        
        return count