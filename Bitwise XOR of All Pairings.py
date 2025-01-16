# https://leetcode.com/problems/bitwise-xor-of-all-pairings/?envType=daily-question&envId=2025-01-16
# Bitwise XOR of All Pairings

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        ans = 0

        if len(nums2) & 1:
            for v in nums1:
                ans ^= v
        if len(nums1) & 1:
            for v in nums2:
                ans ^= v

        return ans