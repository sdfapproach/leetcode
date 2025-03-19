# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/?envType=daily-question&envId=2025-03-19
# Minimum Operations to Make Binary Array Elements Equal to One I

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        k = 3
        ops = 0
        flip = 0
        diff = [0] * n
        
        for i in range(n):
            if i >= k:
                flip ^= diff[i - k]
            
            if (nums[i] ^ flip) == 0:
                if i > n - k:
                    return -1
                ops += 1
                flip ^= 1
                diff[i] = 1
        
        return ops