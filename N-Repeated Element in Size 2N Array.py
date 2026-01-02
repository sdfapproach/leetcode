# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/?envType=daily-question&envId=2026-01-02
# N-Repeated Element in Size 2N Array

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        seen = set()
        
        for num in nums:

            if num in seen:
                return num

            seen.add(num)