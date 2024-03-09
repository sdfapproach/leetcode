# https://leetcode.com/problems/minimum-common-value/?envType=daily-question&envId=2024-03-09
# Minimum Common Value

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        # one = 0
        # two = 0
        
        # while one < len(nums1) and two < len(nums2):
        #     if nums1[one] < nums2[two]:
        #         one += 1
        #     elif nums1[one] > nums2[two]:
        #         two += 1
        #     elif nums1[one] == nums2[two]:
        #         return nums1[one]
        # else:
        #     return -1

        set1 = set(nums1)
        set2 = set(nums2)
        
        commonElements = set1.intersection(set2)
        
        if commonElements:
            return min(commonElements)
        else:
            return -1