# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/?envType=daily-question&envId=2025-06-29
# Number of Subsequences That Satisfy the Given Sum Condition

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()
        
        pow2 = [1] * (n+1)
        for i in range(1, n+1):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        ans = 0
        left, right = 0, n-1
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ans = (ans + pow2[right-left]) % MOD
                left += 1
        
        return ans