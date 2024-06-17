# https://leetcode.com/problems/sum-of-square-numbers/?envType=daily-question&envId=2024-06-17
# Sum of Square Numbers

class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        a = 0

        while a * a <= c:

            b = c - a * a

            if math.isqrt(b) ** 2 == b:
                return True

            a += 1

        return False