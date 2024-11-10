# https://leetcode.com/problems/minimum-array-end/?envType=daily-question&envId=2024-11-09
# Minimum Array End

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        
        n -= 1
        ans = x
        for i in range(31):
            if x >> i & 1 ^ 1:
                ans |= (n & 1) << i
                n >>= 1
        ans |= n << 31
        return ans