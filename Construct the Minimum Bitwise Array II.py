# https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/?envType=daily-question&envId=2026-01-21
# Construct the Minimum Bitwise Array II

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        
        ans = []

        for p in nums:
            if p == 2:
                ans.append(-1)
                continue

            t = 0
            x = p

            while x & 1:
                t += 1
                x >>= 1

            ans.append(p - (1 << (t - 1)))

        return ans