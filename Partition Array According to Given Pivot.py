# https://leetcode.com/problems/partition-array-according-to-given-pivot/?envType=daily-question&envId=2025-03-03
# Partition Array According to Given Pivot

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        return left + middle + right