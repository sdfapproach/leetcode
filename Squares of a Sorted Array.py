# https://leetcode.com/problems/squares-of-a-sorted-array/?envType=daily-question&envId=2024-03-02
# Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        return sorted([n**2 for n in nums])