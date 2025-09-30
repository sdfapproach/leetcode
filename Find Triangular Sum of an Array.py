# https://leetcode.com/problems/find-triangular-sum-of-an-array/?envType=daily-question&envId=2025-09-30
# Find Triangular Sum of an Array

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        tri = [n for n in nums]

        while len(tri) > 1:
            new_tri = []
            for i in range(1, len(tri)):
                new_tri.append((tri[i] + tri[i-1])%10)
            tri = new_tri

        return tri[0]