# https://leetcode.com/problems/find-greatest-common-divisor-of-array/?envType=daily-question&envId=2026-07-18
# Find Greatest Common Divisor of Array

class Solution:
    def findGCD(self, nums: List[int]) -> int:

        nums.sort()
        
        return math.gcd(nums[0], nums[-1])