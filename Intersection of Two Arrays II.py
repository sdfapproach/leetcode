# https://leetcode.com/problems/intersection-of-two-arrays-ii/?envType=daily-question&envId=2024-07-02
# Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort() 
        nums2.sort()

        intersection = []

        i_1 = 0
        i_2 = 0

        while i_1 < len(nums1) and i_2 < len(nums2):

            if nums1[i_1] == nums2[i_2]:
                intersection.append(nums1[i_1])
                i_1 += 1
                i_2 += 1
            elif nums1[i_1] > nums2[i_2]:
                i_2 += 1
            else:
                i_1 += 1

        return intersection

        # count1 = Counter(nums1)
        # count2 = Counter(nums2)

        # intersection = []

        # for num in count1:
        #     if num in count2:
        #         intersection.extend([num] * min(count1[num], count2[num]))

        # return intersection