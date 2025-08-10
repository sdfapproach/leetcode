# https://leetcode.com/problems/reordered-power-of-2/?envType=daily-question&envId=2025-08-10
# Reordered Power of 2

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        def dcount(x: int):
            cnt = [0]*10
            if x == 0:
                cnt[0] = 1
                return cnt
            while x:
                cnt[x % 10] += 1
                x //= 10
            return cnt

        sig = dcount(n)
        L = len(str(n))
        p = 1
        while len(str(p)) <= L:
            if len(str(p)) == L and dcount(p) == sig:
                return True
            p <<= 1
        return False