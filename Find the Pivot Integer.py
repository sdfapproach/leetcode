# https://leetcode.com/problems/find-the-pivot-integer/?envType=daily-question&envId=2024-03-13
# Find the Pivot Integer

class Solution:
    def pivotInteger(self, n: int) -> int:

        if n == 1:
            return 1

        for i in range(n//2, n):

            left = (i+1) * i/2
            right = (i+n) * (n-i+1)/2

            if left == right:
                return i

        return -1