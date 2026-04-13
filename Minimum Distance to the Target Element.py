# https://leetcode.com/problems/minimum-distance-to-the-target-element/description/?envType=daily-question&envId=2026-04-13
# Minimum Distance to the Target Element

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        ans = float('inf')
        
        for i, v in enumerate(nums):
            if v == target:
                ans = min(ans, abs(i - start))
        
        return ans