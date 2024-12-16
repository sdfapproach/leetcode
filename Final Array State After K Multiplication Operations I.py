# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/?envType=daily-question&envId=2024-12-16
# Final Array State After K Multiplication Operations I

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        for _ in range(k):

            idx = nums.index(min(nums))
            nums[idx] = nums[idx] * multiplier

        return nums