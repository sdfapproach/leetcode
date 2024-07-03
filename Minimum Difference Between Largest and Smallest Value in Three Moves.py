# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/?envType=daily-question&envId=2024-07-03
# Minimum Difference Between Largest and Smallest Value in Three Moves

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        n = len(nums)
        
        case1 = nums[n-1] - nums[3]
        case2 = nums[n-2] - nums[2]
        case3 = nums[n-3] - nums[1]
        case4 = nums[n-4] - nums[0]
        
        return min(case1, case2, case3, case4)