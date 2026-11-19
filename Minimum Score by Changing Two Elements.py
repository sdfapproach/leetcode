# https://leetcode.com/problems/minimum-score-by-changing-two-elements/?envType=daily-question&envId=2026-11-19
# Minimum Score by Changing Two Elements

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        
        nums.sort()

        return min(
            nums[-1] - nums[2],
            nums[-2] - nums[1],
            nums[-3] - nums[0]
        )