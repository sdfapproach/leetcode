# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/?envType=daily-question&envId=2025-11-27
# Maximum Subarray Sum With Length Divisible by K

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        
        max_sum = -float('inf')
    
        min_prefix_sum = [float('inf')] * k
        
        min_prefix_sum[0] = 0
        
        current_sum = 0
        
        for i, num in enumerate(nums):
            current_sum += num
            
            remainder = (i + 1) % k
            
            if min_prefix_sum[remainder] != float('inf'):
                max_sum = max(max_sum, current_sum - min_prefix_sum[remainder])
            
            min_prefix_sum[remainder] = min(min_prefix_sum[remainder], current_sum)
                
        return max_sum if max_sum != -float('inf') else 0