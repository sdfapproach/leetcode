# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/?envType=daily-question&envId=2025-02-13
# Minimum Operations to Exceed Threshold Value II

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        ops = 0

        while nums and nums[0] < k:
            if len(nums) < 2:
                return -1
            
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            
            new_val = 2 * x + y
            heapq.heappush(nums, new_val)
            
            ops += 1

        return ops