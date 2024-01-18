# https://leetcode.com/problems/climbing-stairs/?envType=daily-question&envId=2024-01-18
# Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:

        first = 0
        second = 1

        for i in range(n):
            second, first = first + second, second

        return second