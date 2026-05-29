# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/?envType=daily-question&envId=2026-05-29
# Minimum Element After Replacement With Digit Sum

class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        return min(sum(int(n) for n in str(num)) for num in nums)