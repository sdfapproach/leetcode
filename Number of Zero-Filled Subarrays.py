# https://leetcode.com/problems/number-of-zero-filled-subarrays/?envType=daily-question&envId=2025-08-19
# Number of Zero-Filled Subarrays

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        ans = 0
        run = 0

        for x in nums:
            if x == 0:
                run += 1
                ans += run
            else:
                run = 0

        return ans