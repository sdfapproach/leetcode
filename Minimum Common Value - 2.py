# https://leetcode.com/problems/minimum-common-value/?envType=daily-question&envId=2026-05-19
# Minimum Common Value

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        j, i = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        
        return -1