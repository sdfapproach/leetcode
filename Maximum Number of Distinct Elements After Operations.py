# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/?envType=daily-question&envId=2025-10-18
# Maximum Number of Distinct Elements After Operations

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        
        nums.sort()
      
        distinct_count = 0
      
        previous_value = float('-inf')
      
        for num in nums:
           
            current_value = min(num + k, max(num - k, previous_value + 1))
          
            if current_value > previous_value:
                distinct_count += 1
                previous_value = current_value
      
        return distinct_count