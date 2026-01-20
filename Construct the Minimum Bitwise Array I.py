# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/?envType=daily-question&envId=2026-01-20
# Construct the Minimum Bitwise Array I

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        
        ans = []

        for p in nums:
            if p == 2:
                ans.append(-1)
                continue

            t = 0
            temp = p

            while temp & 1:
                t += 1
                temp >>= 1

            ans.append(p - (1 << (t - 1)))

        return ans
