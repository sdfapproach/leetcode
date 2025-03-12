# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/?envType=daily-question&envId=2025-03-12
# Maximum Count of Positive Integer and Negative Integer

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        n = 0
        p = 0

        for num in nums:

            if num < 0:
                n += 1
            elif num > 0:
                p += 1

        return max(n, p)