# https://leetcode.com/problems/greatest-sum-divisible-by-three/?envType=daily-question&envId=2025-11-23
# Greatest Sum Divisible by Three

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        total_sum = sum(nums)
        remainder = total_sum % 3
        
        if remainder == 0:
            return total_sum
        
        rem1 = sorted([n for n in nums if n % 3 == 1])
        rem2 = sorted([n for n in nums if n % 3 == 2])
        
        res = 0
        
        if remainder == 1:
            if rem1:
                res = max(res, total_sum - rem1[0])
            if len(rem2) >= 2:
                res = max(res, total_sum - rem2[0] - rem2[1])
                
        elif remainder == 2:
            if rem2:
                res = max(res, total_sum - rem2[0])
            if len(rem1) >= 2:
                res = max(res, total_sum - rem1[0] - rem1[1])
                
        return res