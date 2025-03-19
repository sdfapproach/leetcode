# https://leetcode.com/problems/divide-array-into-equal-pairs/?envType=daily-question&envId=2025-03-17
# Divide Array Into Equal Pairs

class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        for val in Counter(nums).values():
            if val % 2 != 0:
                return False
        
        return True