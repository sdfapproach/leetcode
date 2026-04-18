# https://leetcode.com/problems/mirror-distance-of-an-integer/?envType=daily-question&envId=2026-04-18
# Mirror Distance of an Integer

class Solution:
    def mirrorDistance(self, n: int) -> int:
        
        return abs(n - int(str(n)[::-1]))