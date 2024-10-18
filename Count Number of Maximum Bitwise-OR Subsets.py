# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/?envType=daily-question&envId=2024-10-18
# Count Number of Maximum Bitwise-OR Subsets

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        max_or = 0

        for num in nums:
            max_or |= num
        
        def countSubsetsWithOr(index, current_or):
            if index == len(nums):
                return 1 if current_or == max_or else 0
            
            include = countSubsetsWithOr(index + 1, current_or | nums[index])
            exclude = countSubsetsWithOr(index + 1, current_or)
            
            return include + exclude

        return countSubsetsWithOr(0, 0)