# https://leetcode.com/problems/count-the-number-of-fair-pairs/?envType=daily-question&envId=2025-04-19
# Count the Number of Fair Pairs

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()
        n = len(nums)
        count = 0
        
        for i in range(n):
            left = bisect.bisect_left(nums, lower - nums[i], i + 1, n)
            right = bisect.bisect_right(nums, upper - nums[i], i + 1, n) - 1
            
            if left <= right:
                count += (right - left + 1)
        
        return count