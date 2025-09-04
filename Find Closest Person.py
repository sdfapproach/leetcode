# https://leetcode.com/problems/find-closest-person/?envType=daily-question&envId=2025-09-04
# Find Closest Person

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        
        a = abs(x-z)
        b = abs(y-z)

        print(a,b)

        if a == b:
            return 0
        elif a < b:
            return 1
        else:
            return 2
