# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/?envType=daily-question&envId=2025-07-17
# Find the Maximum Length of Valid Subsequence II

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        
        count_matrix = [[0] * k for _ in range(k)]
        max_length = 0
      
        for num in nums:
            remainder = num % k
          
            for j in range(k):
                complement_remainder = (j - remainder + k) % k
              
                count_matrix[remainder][complement_remainder] = count_matrix[complement_remainder][remainder] + 1
              
                max_length = max(max_length, count_matrix[remainder][complement_remainder])
      
        return max_length
