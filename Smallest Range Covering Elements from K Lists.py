# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/?envType=daily-question&envId=2024-10-13
# Smallest Range Covering Elements from K Lists

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        min_heap = []
        max_val = float('-inf')
        
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])
        
        result_range = [float('-inf'), float('inf')]
        
        while min_heap:
            min_val, row, col = heapq.heappop(min_heap)
            
            if max_val - min_val < result_range[1] - result_range[0]:
                result_range = [min_val, max_val]
            
            if col + 1 < len(nums[row]):
                next_val = nums[row][col + 1]
                heapq.heappush(min_heap, (next_val, row, col + 1))
                max_val = max(max_val, next_val)
            else:
                break
        
        return result_range