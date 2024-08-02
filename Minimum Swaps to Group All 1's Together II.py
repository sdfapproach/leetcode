# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/?envType=daily-question&envId=2024-08-02
# Minimum Swaps to Group All 1's Together II

class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        k = sum(nums)
    
        if k == 0:
            return 0
        
        nums_extended = nums + nums
        
        current_ones = sum(nums_extended[:k])
        max_ones = current_ones
        
        for i in range(1, len(nums)):
            current_ones = current_ones - nums_extended[i - 1] + nums_extended[i + k - 1]
            max_ones = max(max_ones, current_ones)
        
        return k - max_ones