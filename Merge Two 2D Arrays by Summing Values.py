# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/?envType=daily-question&envId=2025-03-02
# Merge Two 2D Arrays by Summing Values

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        nums = []

        one, two = 0, 0

        while one < len(nums1) and two < len(nums2):

            if nums1[one][0] == nums2[two][0]:

                nums.append([nums1[one][0], nums1[one][1] + nums2[two][1]])
                
                one += 1
                two += 1
            else:
                if nums1[one][0] > nums2[two][0]:
                    nums.append(nums2[two])
                    two += 1
                else:
                    nums.append(nums1[one])
                    one += 1

        
        nums += nums2[two:]
        nums += nums1[one:]
                
        return nums