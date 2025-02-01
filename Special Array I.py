# https://leetcode.com/problems/special-array-i/?envType=daily-question&envId=2025-02-01
# Special Array I

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        if len(nums) < 2:
            return True

        for i in range(1, len(nums)):
            
            if (nums[i-1] + nums[i]) % 2 == 0:
                return False
        
        return True