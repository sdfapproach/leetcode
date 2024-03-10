# https://leetcode.com/problems/intersection-of-two-arrays/?envType=daily-question&envId=2024-03-10
# Intersection of Two Arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        return set1.intersection(set2)