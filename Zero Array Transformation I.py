# https://leetcode.com/problems/zero-array-transformation-i/?envType=daily-question&envId=2025-05-20
# Zero Array Transformation I

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        delta = [0] * (len(nums) + 1)

        for l_idx, r_idx in queries:
            delta[l_idx] += 1
        
            delta[r_idx + 1] -= 1
        
        current_coverage = 0
        for i in range(len(nums)):
            current_coverage += delta[i]
        
            if nums[i] > current_coverage:
                return False
            
        return True