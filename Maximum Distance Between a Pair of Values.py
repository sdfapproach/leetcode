# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/?envType=daily-question&envId=2026-04-19
# Maximum Distance Between a Pair of Values

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        i = j = 0
        ans = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1
        
        return ans