# https://leetcode.com/problems/smallest-missing-multiple-of-k/?envType=daily-question&envId=2026-08-25
# Smallest Missing Multiple of K

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:


        i = 1
        
        while i < 102:
            if k * i not in nums:
                return k * i
            i += 1