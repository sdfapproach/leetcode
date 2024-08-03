# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/?envType=daily-question&envId=2024-08-03
# Make Two Arrays Equal by Reversing Subarrays

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        target.sort()
        arr.sort()

        for i, num in enumerate(target):
            if num != arr [i]:
                return False

        return True