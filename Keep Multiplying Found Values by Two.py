# https://leetcode.com/problems/keep-multiplying-found-values-by-two/?envType=daily-question&envId=2025-11-19
# Keep Multiplying Found Values by Two

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        s = set(nums)

        while original in s:
            original *= 2

        return original