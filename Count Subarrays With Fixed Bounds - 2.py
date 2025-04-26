# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/?envType=daily-question&envId=2025-04-26
# Count Subarrays With Fixed Bounds

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        last_minK = last_maxK = last_invalid = -1
        result = 0
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                last_invalid = i
            
            if num == minK:
                last_minK = i
            if num == maxK:
                last_maxK = i
            
            if last_minK != -1 and last_maxK != -1:
                result += max(0, min(last_minK, last_maxK) - last_invalid)
        
        return result